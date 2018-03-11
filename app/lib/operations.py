import eel
from time import sleep
from . import exposed
from inspect import getmembers, isfunction, isawaitable


def expose_eel():
    exposed_methods = [o[1] for o in getmembers(exposed) if
                       (isfunction(o[1]) or isawaitable(o[1]))]
    for method in exposed_methods:
        eel.expose(method)


def start_eel(should_sleep=True, vue=True):
    eel.init('web')
    if should_sleep:
        sleep(4)
    if vue:
        page = {
            'port': 8081
        }
    else:
        page = 'sample.html'
    eel.start(page, options={
        'port': 8888,
        'host': 'localhost',
    })


def startup():
    expose_eel()
    start_eel(should_sleep=False)
