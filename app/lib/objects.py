import os
import re
import pytz
import msgpack
import json

from . import DictObj
from datetime import datetime
from slugify import slugify


class Message(DictObj):
    pass


class Info(DictObj):
    pass


class StorageObject:
    def _load(self, path, use_list=False):
        with open(path, 'rb') as store:
            return msgpack.load(store, use_list=use_list, encoding='utf-8')

        # with open(path.replace('skppt', 'json'), 'r') as store:
        #     return json.load(store)

    def _dump(self, path, data):
        with open(path, 'wb') as store:
            msgpack.dump(data, store)

        with open(path.replace('skppt', 'json'), 'w') as store:
            json.dump(data, store)


class IndexedStorageObject(StorageObject):
    index = 0
    maximum_recent = 5
    _info_id = None

    def __add__(self, n):
        self.index += n
        self._store_index()
        return self.index

    def _build_path(self, id):
        file_name = '{}.{}.skppt'.format(self.slug, id)
        return os.path.join(self.data_path, file_name)

    def _store_index(self):
        self._dump(self.index_path, self.index)

    def store(self, raw):
        file_path = self._build_path(self.index)
        index = self.index
        data = {
            'id': index,
            'created': datetime.now(tz=pytz.utc).isoformat(),
            'data': raw
        }
        self._dump(file_path, data)
        self += 1
        return index, data

    def update(self, id, raw):
        # if id == self._info_id or self._info_id is None:
        file_path = self._build_path(id)
        data = self.retrieve(id)
        inner_data = data.get('data')
        if isinstance(inner_data, dict):
            data.get('data').update(raw)
        else:
            data['data'] = raw
        self._dump(file_path, data)
        return data
        # else:
        #     raise Exception(f'Cannot update {id}')

    def retrieve(self, id, override=False):
        file_path = self._build_path(id)
        if not os.path.exists(file_path):
            return None
        data = self._load(file_path)
        if data.get('is_deleted', False) and not override:
            return None
        return data

    def recent(self, num=5):
        messages = []
        index = self.index - 1
        num = min(num, self.maximum_recent)
        while len(messages) <= num and index >= 0:
            message = self.get_message(index)
            if message is not None:
                messages.append(message.data)
            index -= 1
        return messages

    def get_message(self, id):
        raw = self.retrieve(id)
        if raw is None:
            return None
        return Message(**raw)


class Store(StorageObject):
    exclusions = ('data', 'path', )

    def __init__(self, data_path):
        self.path = os.path.join(
            data_path,
            'store.skppt'
        )

        if os.path.exists(self.path):
            data = self._load(self.path)
            self.data = DictObj(**data)
        else:
            self.data = DictObj(workspaces=[])
            self.commit()

    def set(self, key, value):
        self.data[key] = value

    def get(self, key, use_list=False):
        data = self._load(self.path, use_list)
        self.data = data
        return data.get(key)

    def commit(self):
        self._dump(self.path, self.data)

    def __setattr__(self, key, val):
        if key not in self.exclusions:
            self.set(key, val)
            self.commit()
        else:
            super().__setattr__(key, val)

    def __getattr__(self, key):
        if key not in self.exclusions:
            return self.get(key)
        else:
            return super().__getattr__(key)


class Session(IndexedStorageObject):
    __info = None

    @classmethod
    def from_slug(cls, slug, session_number, data_path):
        workspace = Workspace.from_slug(slug, data_path)

        return cls(workspace, session_number)

    def __init__(self, workspace, session_number=None):
        if session_number is None:
            create_new = True
            self.session_number = workspace.index
        else:
            self.session_number = session_number
            create_new = False

        self.workspace = workspace
        self.data_path = workspace.data_path
        self.index_path = os.path.join(
            self.data_path,
            f'{workspace.slug}.session.{self.session_number}.idx.skppt'
        )

        if create_new:
            self._store_index()

            workspace.store({
                'id': self.session_number,
                'name': f"Session No. {self.session_number}",
                'slug': self.workspace.slug
            })
        else:
            self.index = self._load(self.index_path)

    def __repr__(self):
        return f'<Session:{self.workspace.slug}:{self.session_number}>'

    def _build_path(self, id):
        file_name = f'{self.workspace.slug}.session.{self.session_number}.{id}.skppt'
        return os.path.join(self.data_path, file_name)

    @property
    def info(self):
        if self.__info is None:
            data = self.workspace.retrieve(id=self.session_number).get('data')
            self.__info = Info(**data)

        return self.__info

    @info.setter
    def info(self, info):
        if not isinstance(info, dict):
            raise AttributeError('info must be an instance of a dict')
        stored = self.workspace.retrieve(id=self.session_number)
        data = stored.get('data')
        data.update(info)
        self.workspace.update(stored.get('id'), data)
        self.__info = None


class Workspace(IndexedStorageObject):
    _info_id = 0
    __info = None

    @classmethod
    def from_slug(cls, slug, data_path):
        regex = r'^([a-z]+)-([a-z]+)-[0-9]+$'
        raw = re.sub(regex, '\\1 \\2', slug, 0)
        name = ' '.join([x.title() for x in raw.split(' ')])

        return cls(name, data_path, slug)

    def __init__(self, workspace_name, data_path, slug=None):
        self.slug = slug \
            if slug is not None \
            else self.make_slug(workspace_name)
        self.name = workspace_name
        self.data_path = data_path
        self.index_path = os.path.join(
            data_path,
            '{}.idx.skppt'.format(self.slug)
        )
        if not os.path.exists(self.index_path):
            self._store_index()

            self._info_id, _ = self.store({
                'name': self.name,
                'slug': self.slug,
                'is_active': False
            })
            self.new_session()
        else:
            self.index = self._load(self.index_path)

    def __repr__(self):
        return f'<Workspace:{self.slug}>'

    @property
    def info(self):
        if self.__info is None:
            data = self.retrieve(id=self._info_id).get('data')
            self.__info = Info(**data)

        return self.__info

    @info.setter
    def info(self, info):
        if not isinstance(info, dict):
            raise AttributeError('info must be an instance of a dict')
        stored = self.retrieve(id=self._info_id)
        data = stored.get('data')
        data.update(info)
        self.update(self._info_id, data)
        self.__info = None

    def recent(self, num=5):
        messages = []
        index = self.index - 1
        num = min(num, self.maximum_recent)
        while len(messages) < num and index > 0:
            message = self.get_message(index)
            if message is not None and message.id != self._info_id:
                messages.append(message.data)
            index -= 1
        return messages

    def new_session(self):
        Session(self)

    def _build_path(self, id):
        file_name = '{}.{}.skppt'.format(self.slug, id)
        return os.path.join(self.data_path, file_name)

    @staticmethod
    def make_slug(text):
        return slugify(text)
