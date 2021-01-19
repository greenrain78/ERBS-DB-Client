import asyncio
import time

from API.api_client import APIClient
from DB import AdaptorDB as DB
from ERBS_token import erbs_api_version, erbs_api_key
from Log.infoLog import logger as log

api_key = erbs_api_key
version = erbs_api_version

sampleList = ['greenrain', 'SinonHecateII', 'tyty6123']


class Engine:
    userNumList = None

    def __init__(self):
        self.API = APIClient(api_key=api_key, version=version)
        DB.initDB()
        # asyncio.run(self.enrollUserList())
        self.initUserList()
        log.info('init %s', __name__)

    def updateGames(self):
        for name in self.userNumList.values():
            asyncio.run(self.updateGames_Num(name))

    async def updateGames_Num(self, num: int):
        log.info('updateGames_Num %d', num)
        nextNum = None
        while True:
            response = await self.API.fetch_user_games_next(num, next=nextNum)
            nextNum = response['next']
            for game in response['games']:
                if DB.checkGameID(game['gameId']):
                    nextNum = None
                    log.info("게임 데이터가 이미 존제: %s", game['gameId'])
                else:
                    DB.insertGames(game)
                    log.info(game)

            log.info(response['next'])
            time.sleep(1)
            if not nextNum:
                break

    async def enrollUserList(self):
        for name in sampleList:
            userNum = await self.API.fetch_user_nickname(name)
            DB.insert(name, userNum)
            log.debug('user name: ', name)

    def initUserList(self):
        tmpList = DB.getUserList()
        self.userNumList = {user[0]: user[1] for user in tmpList}
        log.info(self.userNumList)
