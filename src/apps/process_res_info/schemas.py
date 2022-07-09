import typing

from pydantic import BaseModel

from src.utils.typings import WithoutTzDatetime, DisplayDatetime


class CreateTargetProcessReqModel(BaseModel):
    identify_id: typing.Optional[str]
    pid: int


class CreateTargetProcessResModel(BaseModel):
    id: int
    identify_id: typing.Optional[str]
    pid: int
    name: str
    cmdline: typing.List
    existed: typing.Optional[bool]

    class Config:
        orm_mode = True


class ListTargetProcessResModel(BaseModel):
    id: int
    identify_id: typing.Optional[str]
    pid: int
    name: str
    cmdline: typing.List
    status: int

    class Config:
        orm_mode = True


class StopTargetProcessReqModel(BaseModel):
    identify_id: typing.Optional[str]
    pid: typing.Optional[int]


class StopTargetProcessResModel(BaseModel):
    pid_update_count: int
    identify_id_update_count: int


def list_process_res_info_req_params(
        collected_at_gte: WithoutTzDatetime,
        collected_at_lte: WithoutTzDatetime,
        identify_id: typing.Optional[str] = None,
        pid: typing.Optional[int] = None,
):
    return {
        'collected_at_gte': collected_at_gte,
        'collected_at_lte': collected_at_lte,
        'identify_id': identify_id,
        'pid': pid,
    }


class ListProcessResInfoResModel(BaseModel):
    id: int
    collected_at: DisplayDatetime
    cpu_percent: str
    memory_used: str
    memory_percent: str

    identify_id: typing.Optional[str]
    pid: int
    name: str

    class Config:
        orm_mode = True
