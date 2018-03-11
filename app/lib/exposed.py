from .store import path as storage_path
from .objects import Store
from .objects import Workspace


def get_all_workspace_keys(path=None):
    if path is None:
        path = storage_path

    store = Store(path)
    return store.workspaces


def get_all_workspace_info(path=None):
    if path is None:
        path = storage_path

    keys = get_all_workspace_keys(path=path)
    workspaces = []

    for key in keys:
        wkspc = get_workspace(key, path=path)
        workspaces.append({
            'id': wkspc.info.slug,
            'name': wkspc.info.name,
            'is_active': wkspc.info.is_active,
        })

    return workspaces


def new_workspace(name, path=None):
    if path is None:
        path = storage_path

    store = Store(path)
    workspaces = store.get('workspaces', use_list=True)

    new_workspace = Workspace(name, path)
    workspaces.append(new_workspace.slug)
    store.set('workspaces', workspaces)
    store.commit()


def get_workspace(name, path=None):
    if path is None:
        path = storage_path

    workspace = Workspace(name, path)
    return workspace


def update_workspace(name, key, value, path=None):
    workspace = get_workspace(name, path=path)
    workspace.info = {key: value}
