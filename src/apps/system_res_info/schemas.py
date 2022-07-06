import typing
from datetime import datetime

from pydantic import BaseModel, validator

from src.utils.typings import DisplayDatetime


class ListSystemResInfoResModel(BaseModel):
    id: int
    # collected_at: typing.Union[datetime, int]
    collected_at: DisplayDatetime
    cpu_percent: str
    memory_used: str
    memory_percent: str

    class Config:
        orm_mode = True

    # @validator('collected_at')
    # def dt_2_ts(cls, v):
    #     return dt2ts(v)
