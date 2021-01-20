from time import sleep

from Log.infoLog import logger as log
import MainScheduler
from Settings import debug, on_MariaDB, on_sqlDB

if __name__ == '__main__':
    log.info('status debug: %s, mariaDB: %s, sqlDB: %s', debug, on_MariaDB, on_sqlDB)
    log.info('run __main__')
    MainScheduler.start()

    log.info('run while')
    while True:
        log.debug("Running main process...............")
        sleep(60*60)
