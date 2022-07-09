import typing
from datetime import datetime
from decimal import Decimal

from sqlalchemy import asc, desc

from src.utils.date_and_time import str2datetime
from .db import LocalSession
from .models import SystemResInfo, TargetProcess, ProcessResInfo


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
    return system_res_info.save(db)


def list_system_res_info(
        db: LocalSession,
        collected_at_gte: datetime = None,
        collected_at_lte: datetime = None,
        order_by=asc(SystemResInfo.collected_at),
) -> typing.List[SystemResInfo]:
    queryset = db.query(SystemResInfo)
    if collected_at_gte:
        queryset = queryset.filter(SystemResInfo.collected_at >= collected_at_gte)
    if collected_at_lte:
        queryset = queryset.filter(SystemResInfo.collected_at <= collected_at_lte)
    return queryset.order_by(order_by).all()


def create_target_process(
        db: LocalSession,
        identify_id=None,
        pid=None,
        name=None,
        cmdline=None,
):
    target_process = TargetProcess(
        identify_id=identify_id,
        pid=pid,
        name=name,
        cmdline=cmdline,
    )
    return target_process.save(db)


def retrieve_target_process(
        db: LocalSession,
        *filter_args,
) -> typing.Optional[TargetProcess]:
    return db.query(TargetProcess).filter(*filter_args).first()


def list_process_res_info(
        db: LocalSession,
        collected_at_gte: datetime = None,
        collected_at_lte: datetime = None,
        identify_id: str = None,
        pid: int = None,
        order_by=asc(ProcessResInfo.collected_at),
) -> typing.List[ProcessResInfo]:
    queryset = db.query(
        ProcessResInfo.id.label('id'),
        ProcessResInfo.target_process_id.label('target_process_id'),
        ProcessResInfo.collected_at.label('collected_at'),
        ProcessResInfo.cpu_percent.label('cpu_percent'),
        ProcessResInfo.memory_used.label('memory_used'),
        ProcessResInfo.memory_percent.label('memory_percent'),
        TargetProcess.identify_id.label('identify_id'),
        TargetProcess.pid.label('pid'),
        TargetProcess.name.label('name'),
    ).join(TargetProcess, TargetProcess.id == ProcessResInfo.target_process_id)
    if collected_at_gte:
        queryset = queryset.filter(ProcessResInfo.collected_at >= collected_at_gte)
    if collected_at_lte:
        queryset = queryset.filter(ProcessResInfo.collected_at <= collected_at_lte)
    if identify_id:
        queryset = queryset.filter(TargetProcess.identify_id == identify_id)
    if isinstance(pid, int):
        queryset = queryset.filter(TargetProcess.pid == pid)
    return queryset.order_by(order_by).all()
