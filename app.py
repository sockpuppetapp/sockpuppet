import eel
import threading
from subprocess import call
from time import sleep


eel.init('web')


@eel.expose
def add(x, y):
    z = x + y
    print('{} + {} = {}'.format(x, y, z))

def start_web():
    call(['./start.sh'])


def start_eel(should_sleep=True, vue=True):
    if should_sleep:
        sleep(4)
    if vue:
        page = {
            'port': 8080
        }
    else:
        page = 'sample.html'
    eel.start(page, options={
        'port': 8888,
        'host': 'localhost',
    })


if __name__ == '__main__':
    # t1 = threading.Thread(target=start_web)
    # t2 = threading.Thread(target=start_eel)
    # t1.start()
    # t2.start()
    start_eel(should_sleep=False, vue=True)
