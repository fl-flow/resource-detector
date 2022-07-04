import os
import _thread

import uvicorn

from src.settings.base import LOCAL_DATABASE_URL
from src.databases.local.db import Base
from src.tasks.res_info import collect_host_machine_info_task


def init_local_db():
    if not os.path.exists(LOCAL_DATABASE_URL):
        Base.metadata.create_all()


def start_task():
    _thread.start_new_thread(collect_host_machine_info_task, ())


def start_http_server():
    uvicorn.run('src.main:app', host='0.0.0.0', port=8000, workers=1)


if __name__ == '__main__':
    init_local_db()
    start_task()
    start_http_server()
