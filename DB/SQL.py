from Settings import debug
from Log.infoLog import logger as log

if not debug:
    gamesTableName = 'ERBS_games'
    userTableName = 'ERBS_user'
    stateTableName = 'ERBS_state'
else:
    gamesTableName = 'test_ERBS_games'
    userTableName = 'test_ERBS_user'
    stateTableName = 'test_ERBS_state'

gamesTable = {"userNum": 'INT',
              "nickname": 'VARCHAR(255)',
              "gameId": 'INT',
              "seasonId": 'INT',
              "matchingMode": 'INT',
              "matchingTeamMode": 'INT',
              "characterNum": 'INT',
              "characterLevel": 'INT',
              "gameRank": 'INT',
              "playerKill": 'INT',
              "playerAssistant": 'INT',
              "monsterKill": 'INT',
              "bestWeapon": 'INT',
              "bestWeaponLevel": 'INT',
              "masteryLevel": 'JSON',
              "equipment": 'JSON',
              "versionMajor": 'INT',
              "versionMinor": 'INT',
              "skillLevelInfo": 'JSON',
              "skillOrderInfo": 'JSON',
              "serverName": 'JSON',
              "maxHp": 'INT',
              "maxSp": 'INT',
              "attackPower": 'INT',
              "defense": 'INT',
              "hpRegen": 'REAL',
              "spRegen": 'REAL',
              "attackSpeed": 'REAL',
              "moveSpeed": 'REAL',
              "outOfCombatMoveSpeed": 'REAL',
              "sightRange": 'REAL',
              "attackRange": 'REAL',
              "criticalStrikeChance": 'REAL',
              "criticalStrikeDamage": 'REAL',
              "coolDownReduction": 'REAL',
              "lifeSteal": 'REAL',
              "amplifierToMonster": 'REAL',
              "trapDamage": 'REAL',
              "gainExp": 'INT',
              "startDtm": 'datetime',
              "duration": 'INT',
              "mmrBefore": 'INT',
              "damageToPlayer": 'INT',
              "damageToMonster": 'INT',
              "killerUserNum": 'INT',
              "playTime": 'INT',
              "watchTime": 'INT',
              "totalTime": 'INT',
              "botAdded": 'INT',
              "botRemain": 'INT',
              "restrictedAreaAccelerated": 'INT',
              "safeAreas": 'INT',
              "killer": 'VARCHAR(255)',
              "killDetail": 'VARCHAR(255)',
              "causeOfDeath": "VARCHAR(255)",
              "teamNumber": 'INT',
              "preMade": 'INT',
              "gainedNormalMmrKFactor": 'REAL',
              "victory": 'INT',
              "craftUncommon": 'INT',
              "craftRare": 'INT',
              "craftEpic": 'INT',
              "craftLegend": 'INT',
              "trapDamageToPlayer": 'INT',
              "basicAttackDamageToPlayer": 'INT',
              "skillDamageToPlayer": 'INT',
              }

# make DB table init SQL
# games
initGamesSQL = f'CREATE TABLE IF NOT EXISTS {gamesTableName}('
i = 1
for key, val in gamesTable.items():
    if i != len(gamesTable):
        initGamesSQL += f'{key} {val}, '
    else:
        initGamesSQL += f'{key} {val}'
    i = i + 1
initGamesSQL += f');'
log.debug(initGamesSQL)

# user
initUserSQL = f'CREATE TABLE IF NOT EXISTS {userTableName}( ' \
              f'no      INT NOT NULL AUTO_INCREMENT PRIMARY KEY, ' \
              f'name    VARCHAR(255) NOT NULL, ' \
              f'userNum INT     NOT NULL, ' \
              f'time  datetime  NOT NULL DEFAULT CURRENT_TIMESTAMP' \
              f');'
log.debug(initUserSQL)
