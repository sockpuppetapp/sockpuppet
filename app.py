import eel
import threading
from subprocess import call
from time import sleep


def start_web():
    call(['./start.sh'])


def start_eel():
    sleep(4)
    eel.init('web')
    eel.start('', options={
        'port': 8080,
        'host': 'localhost',
    })


if __name__ == '__main__':
    t1 = threading.Thread(target=start_web)
    t2 = threading.Thread(target=start_eel)
    t1.start()
    t2.start()
