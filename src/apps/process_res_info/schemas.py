import typing

from pydantic import BaseModel


class CreateTargetProcessReqModel(BaseModel):
    identify_id: typing.Optional[str]
    pid: int


class CreateTargetProcessResModel(BaseModel):
    id: int
    identify_id: typing.Optional[str]
    pid: int
    name: typing.Optional[str]
    cmdline: typing.Optional[typing.List]

    class Config:
        orm_mode = True
