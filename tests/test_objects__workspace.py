from app.lib.objects import Workspace
from app.lib.objects import DictObj
import msgpack
import pytest


@pytest.fixture
def workspace(tmpdir):
    name = 'Sample'
    return Workspace(name, tmpdir)


def test_workspace_init(tmpdir, workspace):
    name = 'Sample'
    index_file = tmpdir.join(f'{name.lower()}.skppt')
    info_file = tmpdir.join(f'{name.lower()}.1.skppt')

    assert isinstance(workspace, Workspace)
    assert index_file.exists()
    assert info_file.exists()
    assert index_file == workspace.index_path

    assert workspace._Workspace__info_id == 1

    with open(info_file, 'rb') as store:
        info = msgpack. \
            load(store, use_list=False, encoding='utf-8'). \
            get('data')

    assert info == workspace.info
    assert name.lower() == workspace.slug
    assert name == workspace.name


def test_workspace_info_updates_as_property(workspace):
    assert workspace.info.is_active is False
    workspace.info.is_active = True
    assert workspace.info.is_active is True


def test_workspace_info_updates_as_set(workspace):
    assert workspace.info.is_active is False
    workspace.info = {'foo': 'bar'}
    assert workspace.info.is_active is False
    assert workspace.info.foo == 'bar'


def test_workspace_store_message(workspace):
    text = 'This is a message'
    id, _ = workspace.store(text)
    msg = workspace.get_message(id)

    assert id == 2
    assert isinstance(msg, DictObj)
    assert msg.data == text


def test_workspace_from_slug(tmpdir):
    slug = "foo-bar-9999"
    workspace = Workspace.from_slug(slug, tmpdir)

    assert isinstance(workspace, Workspace)
    assert workspace.slug == slug
    assert workspace.name == 'Foo Bar'
