import typing

from fastapi import APIRouter, Depends

from src.apps.process_res_info.schemas import (
    CreateTargetProcessReqModel, CreateTargetProcessResModel,
)
from src.databases.local import dao
from src.databases.local.db import LocalSession, get_local_db

process_res_info_router = APIRouter()


@process_res_info_router.post('/target_process/', response_model=CreateTargetProcessResModel)
def create_target_process(
        req_data: CreateTargetProcessReqModel,
        db: LocalSession = Depends(get_local_db),
):
    return dao.create_target_process(db, **req_data.dict())
