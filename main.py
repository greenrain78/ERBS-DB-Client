from time import sleep

from Log.infoLog import logger as log
import MainScheduler

if __name__ == '__main__':
    log.info('run __main__')
    MainScheduler.start()

    while True:
        print("Running main process...............")
        sleep(10)
