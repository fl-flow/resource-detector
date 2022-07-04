from datetime import datetime
from decimal import Decimal

from .db import Session
from .models import SystemResInfo


def create_system_res_info(
        collected_at: datetime,
        cpu_percent,
        memory_used,
        memory_percent,
        session: Session = None,
):
    session = session or Session()
    system_res_info = SystemResInfo(
        collected_at=collected_at,
        cpu_percent=Decimal(str(cpu_percent)),
        memory_used=Decimal(str(memory_used)),
        memory_percent=Decimal(str(memory_percent)),
    )
    session.add(system_res_info)
    session.commit()
