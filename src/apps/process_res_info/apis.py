import typing
from datetime import datetime

import psutil
from fastapi import APIRouter, Depends, HTTPException, exceptions
from sqlalchemy import desc

from src.apps.process_res_info.schemas import (
    CreateTargetProcessReqModel, CreateTargetProcessResModel,
    ListTargetProcessResModel,
    StopTargetProcessReqModel, StopTargetProcessResModel,
    list_process_res_info_req_params, ListProcessResInfoResModel,
)
from src.databases.local import dao
from src.databases.local.db import LocalSession, get_local_db
from src.databases.local.models import TargetProcess
from src.utils.typings import WithoutTzDatetime

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
    # identify_id = create_data.get('identify_id')
    identify_id = req_data.identify_id
    if identify_id:
        # existed_target_process: TargetProcess = db.query(TargetProcess).filter(TargetProcess.identify_id == identify_id).first()
        existed_target_process: TargetProcess = dao.retrieve_target_process(db, TargetProcess.identify_id == identify_id)
        if existed_target_process:
            existed_target_process.pid = pid
            existed_target_process.name = p_name
            existed_target_process.cmdline = p_cmdline
            existed_target_process.status = TargetProcess.StatusChoices.monitoring
            existed_target_process.save(db)
            setattr(existed_target_process, 'existed', True)
            return existed_target_process

    create_data.update({
        'name': p.name(),
        'cmdline': p.cmdline(),
    })
    return dao.create_target_process(db, **create_data)


@process_res_info_router.get('/target_process/', response_model=typing.List[ListTargetProcessResModel])
def list_target_process(
        status: typing.Optional[int] = None,
        db: LocalSession = Depends(get_local_db),
):
    queryset = db.query(TargetProcess)
    if status:
        queryset = queryset.filter(TargetProcess.status == status)
    return queryset.order_by(desc(TargetProcess.updated_at)).all()


@process_res_info_router.post('/stop_target_process/', response_model=StopTargetProcessResModel)
def stop_target_process(
        req_data: StopTargetProcessReqModel,
        db: LocalSession = Depends(get_local_db),
):
    update_data = {'status': TargetProcess.StatusChoices.stopped, 'updated_at': datetime.now()}
    queryset = db.query(TargetProcess).filter(TargetProcess.status == TargetProcess.StatusChoices.monitoring)
    identify_id_update_count = 0
    pid_update_count = 0
    if req_data.identify_id:
        identify_id_update_count = queryset.filter(TargetProcess.identify_id == req_data.identify_id).update(update_data)
        db.commit()
    if req_data.pid:
        pid_update_count = queryset.filter(TargetProcess.pid == req_data.pid).update(update_data)
        db.commit()
    return {'pid_update_count': pid_update_count, 'identify_id_update_count': identify_id_update_count}


@process_res_info_router.get('/', response_model=typing.List[ListProcessResInfoResModel])
def list_process_res_info(
        params=Depends(list_process_res_info_req_params),
        db: LocalSession = Depends(get_local_db),
):
    data_list = dao.list_process_res_info(db, **params)
    return data_list
