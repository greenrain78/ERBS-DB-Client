from datetime import datetime
from typing import List

from DB.SQL import initGamesSQL, initUserSQL, userTableName, gamesTableName, gamesTable
from DB.mariaDB import runSQL, getSQL
from DB.DBLog import getLogger

log = getLogger()


def initDB():
    # init DB
    runSQL(initGamesSQL)
    runSQL(initUserSQL)
    log.info('init DB in [%s]', __name__)


def insert(name: str, userNum: int):
    sql = f'insert into {userTableName} ' \
          f'(name, userNum) values(' \
          f'"{name}", {userNum})'
    runSQL(sql)
    log.debug(f"{name} insert userNum{userNum}")


def getUserList() -> List[tuple]:
    sql = f"select name, userNum from {userTableName}"
    result = getSQL(sql)
    return result


def insertGames(data: dict):
    # games
    sql = f'insert into {gamesTableName}('
    for key in data:
        sql += f'{key}, '
    sql = sql[:-2] + ') values( '

    for key, val in data.items():
        if key == 'startDtm':
            val = val.translate({ord('T'): ' '})
            val = val[:-5]
            print(val)
            val = datetime.strptime(val, '%Y-%m-%d %H:%M:%S.%f')
            log.debug(f"test: {val}")
            sql += f'"{val}", '
        elif type(val) is str:
            sql += f'"{val}", '
        elif type(val) is dict:
            sql += f'"{val}", '
        else:
            sql += f'{val}, '
    sql = sql[:-2] + ')'
    runSQL(sql)
    log.debug(f"insertGames user({data['nickname']})game:{data['gameId']}")


def getGameID() -> int:
    sql = f"select gameId from {gamesTableName} ORDER BY gameId DESC LIMIT 1"
    result = getSQL(sql)
    if not result:
        return None
    else:
        return result[0][0]


def checkGameID(gameID: int, userNum: int) -> bool:
    sql = f"select gameId from {gamesTableName} WHERE gameId = {gameID} AND userNum = {userNum} "
    result = getSQL(sql)
    print(result)
    if not result:
        return False
    else:
        return True
