import sqlalchemy
from sqlalchemy import (
    Column, Integer, String, DateTime,
    DECIMAL,
    BigInteger,  # Sqlite doesn't allow BIGINT used as an primary key with autoincrement.
    ForeignKey,
    JSON,
)
from sqlalchemy.orm import relationship, backref

from src.databases.models import CommonMixin, DatetimeMixin
from .db import LocalBase


class SystemResInfo(CommonMixin, LocalBase):
    __tablename__ = 'system_res_info'

    id = Column(Integer, primary_key=True)
    collected_at = Column(DateTime, index=True)
    cpu_percent = Column(DECIMAL(8, 2))
    memory_used = Column(DECIMAL(16, 2), comment='MB')
    memory_percent = Column(DECIMAL(8, 2))


class TargetProcess(CommonMixin, DatetimeMixin, LocalBase):
    __tablename__ = 'target_process'

    id = Column(Integer, primary_key=True)
    identify_id = Column(String(128), index=True)
    pid = Column(Integer)
    name = Column(String(128))
    cmdline = Column(JSON, comment='cmdline list')


class ProcessResInfo(CommonMixin, LocalBase):
    __tablename__ = 'process_res_info'

    id = Column(Integer, primary_key=True)
    # target_process_id = Column(Integer, ForeignKey('target_process.id'))
    # target_process = relationship('TargetProcess', backref=backref('res_info_records'))
    # without constraint:
    target_process_id = Column(Integer, index=True)
    target_process = relationship(
        'TargetProcess',
        foreign_keys=[target_process_id],
        primaryjoin='TargetProcess.id == ProcessResInfo.target_process_id',
        backref=backref('res_info_records'),
    )
    collected_at = Column(DateTime, index=True)
    cpu_percent = Column(DECIMAL(8, 2))
    memory_used = Column(DECIMAL(16, 2), comment='MB')
    memory_percent = Column(DECIMAL(8, 2))
