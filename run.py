import os
import _thread

import uvicorn
from loguru import logger

from src.settings.base import LOCAL_DATABASE_URL, DEBUG
from src.databases.local.db import LocalBase
from src.tasks.res_info import collect_host_machine_info_task

if not os.path.exists('log'):
    os.mkdir('log')

logger.add('log/common.log', rotation='50 MB', retention=1)
logger.add('log/error.log', rotation='50 MB', retention=1, level='ERROR')


def init_local_db():
    if not os.path.exists(LOCAL_DATABASE_URL):
        LocalBase.metadata.create_all()
    LocalBase.metadata.create_all()


def start_task():
    _thread.start_new_thread(collect_host_machine_info_task, ())


def start_http_server():
    uvicorn.run('src.main:app', host='0.0.0.0', port=7777, workers=1, debug=DEBUG)


if __name__ == '__main__':
    init_local_db()
    start_task()
    start_http_server()
