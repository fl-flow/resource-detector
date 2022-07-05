import typing
from datetime import datetime
from decimal import Decimal

from src.utils.date_and_time import str2datetime
from .db import LocalSession
from .models import SystemResInfo


def create_system_res_info(
        db: LocalSession,
        collected_at: datetime,
        cpu_percent,
        memory_used,
        memory_percent,
) -> SystemResInfo:
    system_res_info = SystemResInfo(
        collected_at=collected_at,
        cpu_percent=Decimal(str(cpu_percent)),
        memory_used=Decimal(str(memory_used)),
        memory_percent=Decimal(str(memory_percent)),
    )
    db.add(system_res_info)
    db.commit()
    db.refresh(system_res_info)
    return system_res_info


def list_system_res_info(
        db: LocalSession,
        collected_at_gte: datetime = None,
        collected_at_lte: datetime = None,
) -> typing.List[SystemResInfo]:
    queryset = db.query(SystemResInfo)
    if collected_at_gte:
        queryset = queryset.filter(SystemResInfo.collected_at >= collected_at_gte)
    if collected_at_lte:
        queryset = queryset.filter(SystemResInfo.collected_at <= collected_at_lte)
    return queryset.all()
