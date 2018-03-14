from .store import path as storage_path
from .objects import Store
from .objects import Workspace
from .objects import Session


def get_all_workspace_keys(path=None):
    if path is None:  # noqa
        path = storage_path

    store = Store(path)
    return store.workspaces


def get_all_workspace_info(path=None):
    if path is None:  # noqa
        path = storage_path

    keys = get_all_workspace_keys(path=path)
    workspaces = []

    for key in keys:
        wkspc = get_workspace(key, path=path)
        workspaces.append({
            'id': wkspc.info.slug,
            'name': wkspc.info.name,
            'is_active': wkspc.info.is_active,
            'sessions': wkspc.recent(),
        })

    return workspaces


def new_workspace(name, slug=None, path=None):
    if path is None:  # noqa
        path = storage_path

    store = Store(path)
    workspaces = store.get('workspaces', use_list=True)

    new_workspace = Workspace(name, path, slug=slug)
    workspaces.append(new_workspace.slug)
    store.set('workspaces', workspaces)
    store.commit()


def get_workspace(slug, path=None):
    if path is None:  # noqa
        path = storage_path

    workspace = Workspace.from_slug(slug, path)
    return workspace


def update_workspace(slug, key, value, path=None):
    if path is None:  # noqa
        path = storage_path

    workspace = get_workspace(slug, path=path)
    workspace.info = {key: value}


def get_session(slug, session_number, path=None):
    if path is None:  # noqa
        path = storage_path

    session = Session.from_slug(slug, session_number, path)
    return session


def new_session(slug, path=None):
    if path is None:  # noqa
        path = storage_path

    workspace = Workspace.from_slug(slug, path)
    workspace.new_session()


def update_session(slug, session_number, key, value, path=None):
    if path is None:  # noqa
        path = storage_path

    session = get_session(slug, session_number, path=path)
    session.info = {key: value}
