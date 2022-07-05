import sqlalchemy
from sqlalchemy import Column, Integer, DateTime, DECIMAL, BigInteger

from .db import LocalBase


class SystemResInfo(LocalBase):
    __tablename__ = 'system_res_info'

    id = Column(BigInteger, primary_key=True)
    collected_at = Column(DateTime, index=True)
    cpu_percent = Column(DECIMAL(8, 2))
    memory_used = Column(DECIMAL(16, 2))  # 单位 MB
    memory_percent = Column(DECIMAL(8, 2))
