from datetime import time

from apscheduler.schedulers.background import BackgroundScheduler
from Log.infoLog import logger as log
from baseEngine import Engine

schedule = BackgroundScheduler()
engine = Engine()


# 매일
# @schedule.scheduled_job('cron', hour='12', id='every day check')
@schedule.scheduled_job('cron', args=None, second='12', id='every day check')
def updateGames():
    log.info('start updateGames')
    engine.updateGames()
    log.info('end updateGames')


def start():
    schedule.start()
    log.info("start scheduler")
