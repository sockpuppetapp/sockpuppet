from app.lib.exposed import get_all_workspace_info
from app.lib.exposed import get_all_workspace_keys
from app.lib.exposed import get_workspace
from app.lib.exposed import new_workspace
from app.lib.exposed import update_workspace
from app.lib.objects import Store
import pytest


name = 'Sample'
slug = 'sample'


@pytest.fixture
def store(tmpdir):
    return tmpdir, Store(tmpdir)


def test_new_workspace(store):
    tmpdir, store = store
    new_workspace(name, path=tmpdir)

    assert name.lower() in store.get('workspaces')
    assert name.lower() in store.workspaces


def test_get_all_workspace_keys(store):
    tmpdir, _ = store
    new_workspace(name, path=tmpdir)
    workspaces = get_all_workspace_keys(path=tmpdir)

    assert name.lower() in workspaces


def test_get_workspace(store):
    tmpdir, _ = store
    new_workspace(name, path=tmpdir)
    workspace = get_workspace(slug, path=tmpdir)

    assert workspace.name == name
    assert workspace.slug == name.lower()


def test_get_all_workspace_info(store):
    tmpdir, _ = store

    new_workspace(name, path=tmpdir)
    info = get_all_workspace_info(path=tmpdir)

    keys = ('id', 'name', 'is_active')

    assert isinstance(info, list)
    assert len(info) > 0
    assert all(
        key in x.keys()
        for x in info
        for key in keys
    )


# def update_workspace(name, key, value, path=None):
def test_update_workspace(store):
    tmpdir, _ = store

    workspace = get_workspace(slug, path=tmpdir)
    assert 'foobar' not in workspace.info

    update_workspace(slug, 'foobar', 1, path=tmpdir)

    workspace = get_workspace(slug, path=tmpdir)
    assert 'foobar' in workspace.info
    assert workspace.info.foobar == 1

    update_workspace(slug, 'foobar', 2, path=tmpdir)

    workspace = get_workspace(slug, path=tmpdir)
    assert 'foobar' in workspace.info
    assert workspace.info.foobar == 2
