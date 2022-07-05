import time
from datetime import datetime

import psutil
from loguru import logger

from src.databases.local.dao import create_system_res_info


def collect_host_machine_info_task():
    while True:
        cpu_percent = psutil.cpu_percent()
        virtual_memory = psutil.virtual_memory()
        memory_percent = virtual_memory.percent
        # memory_used = round(virtual_memory.used / 1024 / 1024, 2)
        memory_used = round(virtual_memory.total * memory_percent / 100 / 1024 / 1024, 2)

        log_ctx = {
            'cpu_percent': cpu_percent,
            'memory_used(MB)': f'{memory_used} MB',
            'memory_percent': memory_percent,
        }

        create_system_res_info(
            collected_at=datetime.now(),
            cpu_percent=cpu_percent,
            memory_used=memory_used,
            memory_percent=memory_percent,
        )

        logger.info(log_ctx)
        time.sleep(60)


if __name__ == '__main__':
    collect_host_machine_info_task()
