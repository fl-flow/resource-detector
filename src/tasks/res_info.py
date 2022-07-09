import time
import typing
from datetime import datetime

import psutil
from loguru import logger

from src.databases.local.dao import create_system_res_info
from src.databases.local.db import LocalSession
from src.databases.local.models import TargetProcess, ProcessResInfo


def collect_host_machine_info_task():
    while True:
        try:
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

            db = LocalSession()
            create_system_res_info(
                db=db,
                collected_at=datetime.now(),
                cpu_percent=cpu_percent,
                memory_used=memory_used,
                memory_percent=memory_percent,
            )
            db.close()

            logger.info(log_ctx)
        except Exception as e:
            logger.error(e)
        time.sleep(60)


def collect_target_process_info_task():
    while True:
        try:
            db = LocalSession()
            target_process_objs: typing.List[TargetProcess] = db.query(TargetProcess).filter(TargetProcess.status == TargetProcess.StatusChoices.monitoring).all()

            memory_total = psutil.virtual_memory().total

            for target_process in target_process_objs:
                log_ctx = {
                    'pid': target_process.pid,
                }
                try:
                    p = psutil.Process(target_process.pid)
                    cpu_percent = p.cpu_percent(0.1)
                    rss_memory = p.memory_info().rss
                    rss_memory_used_mb = round(rss_memory / 1024 / 1024, 2)
                    rss_memory_used_percent = round(rss_memory / memory_total * 100, 2)

                    process_res_info = ProcessResInfo()
                    process_res_info.target_process_id = target_process.id
                    process_res_info.collected_at = datetime.now()
                    process_res_info.cpu_percent = cpu_percent
                    process_res_info.memory_used = rss_memory_used_mb
                    process_res_info.memory_percent = rss_memory_used_percent
                    process_res_info.save(db)

                    log_ctx.update({
                        'cpu_percent': cpu_percent,
                        'rss_memory_used_mb': f'{rss_memory_used_mb} MB',
                        'rss_memory_used_percent': rss_memory_used_percent,
                    })
                    logger.info(log_ctx)
                except Exception as e:
                    target_process.status = TargetProcess.StatusChoices.error
                    target_process.save(db)
                    log_ctx.update({
                        'e': e,
                    })
                    logger.error(log_ctx)
            db.close()
        except Exception as e:
            logger.error(e)
        time.sleep(60)


if __name__ == '__main__':
    # collect_host_machine_info_task()
    collect_target_process_info_task()
