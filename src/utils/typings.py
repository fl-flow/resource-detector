from datetime import datetime

from src.utils.date_and_time import dt2ts


class DisplayDatetime(datetime):
    """
    datetime 数据类型，展示时希望转成时间戳
    """

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        return dt2ts(v)
