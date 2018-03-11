from app.lib.exposed import get_all_workspace_keys
from app.lib.exposed import get_workspace
from app.lib.exposed import set_workspace
from app.lib.objects import Store
import pytest


name = 'Sample'


@pytest.fixture
def store(tmpdir):
    return tmpdir, Store(tmpdir)


def test_set_workspace(store):
    tmpdir, store = store
    set_workspace(name, path=tmpdir)

    assert name.lower() in store.get('workspaces').get('available')
    assert name.lower() in store.workspaces.get('available')


def test_get_all_workspace_keys(store):
    tmpdir, store = store
    set_workspace(name, path=tmpdir)
    workspaces = get_all_workspace_keys(path=tmpdir)

    assert name.lower() in workspaces


def test_get_workspace(store):
    tmpdir, store = store
    set_workspace(name, path=tmpdir)
    workspace = get_workspace(name, path=tmpdir)

    assert workspace.name == name
    assert workspace.slug == name.lower()
