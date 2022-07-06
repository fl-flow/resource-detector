import typing

import psutil
from fastapi import APIRouter, Depends, HTTPException, exceptions

from src.apps.process_res_info.schemas import (
    CreateTargetProcessReqModel, CreateTargetProcessResModel,
)
from src.databases.local import dao
from src.databases.local.db import LocalSession, get_local_db
from src.databases.local.models import TargetProcess

process_res_info_router = APIRouter()


@process_res_info_router.post('/target_process/', response_model=CreateTargetProcessResModel)
def create_target_process(
        req_data: CreateTargetProcessReqModel,
        db: LocalSession = Depends(get_local_db),
):
    pid = req_data.pid
    try:
        p = psutil.Process(pid)
        p_name = p.name()
        p_cmdline = p.cmdline()
    except Exception as e:
        raise HTTPException(400, repr(e))

    create_data: dict = req_data.dict()
    identify_id = create_data.get('identify_id')
    if identify_id:
        # existed_target_process: TargetProcess = db.query(TargetProcess).filter(TargetProcess.identify_id == identify_id).first()
        existed_target_process: TargetProcess = dao.retrieve_target_process(db, TargetProcess.identify_id == identify_id)
        if existed_target_process:
            existed_target_process.pid = pid
            existed_target_process.name = p_name
            existed_target_process.cmdline = p_cmdline
            existed_target_process.status = TargetProcess.StatusChoices.monitoring
            existed_target_process.save(db)
            return existed_target_process

    create_data.update({
        'name': p.name(),
        'cmdline': p.cmdline(),
    })
    return dao.create_target_process(db, **create_data)
