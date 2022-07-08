import typing

from pydantic import BaseModel


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
