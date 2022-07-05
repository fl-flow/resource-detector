import typing
from datetime import datetime

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder

from src.databases.local import dao
from src.databases.local.db import LocalSession, get_local_db
from src.utils.typings import WithoutTzDatetime
from .schemas import SystemResInfoListResModel

system_res_info_router = APIRouter()


@system_res_info_router.get('/', response_model=typing.List[SystemResInfoListResModel])
def list_system_res_info(
        collected_at_gte: WithoutTzDatetime,
        collected_at_lte: WithoutTzDatetime,
        db: LocalSession = Depends(get_local_db),
):
    return dao.list_system_res_info(db, collected_at_gte, collected_at_lte)
