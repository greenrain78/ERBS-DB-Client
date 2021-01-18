from Log.infoLog import logger as log
from api_client import APIClient
from token import erbs_api_key, erbs_api_version

api_key = erbs_api_key
version = erbs_api_version

if __name__ == '__main__':
    erbsAPI = APIClient(api_key=api_key, version=version)

