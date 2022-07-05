import time
import typing
from datetime import date, datetime
from typing import Union


def dt2ts(dt: datetime, return_int_with_second=True) -> Union[int, float]:
    ts = time.mktime(dt.timetuple())
    if return_int_with_second:
        return int(ts)
    return ts


def str2datetime(s: typing.Union[str, int], format='%Y-%m-%d') -> Union[datetime, None]:
    """
    日期型字符转datetime，支持时间戳
    """
    if isinstance(s, datetime):
        return s
    try:
        return datetime.strptime(s, format)
    except:
        pass
    try:
        return datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
    except:
        pass
    try:
        return datetime.fromtimestamp(int(s))
    except:
        pass
    try:
        return datetime.fromtimestamp(int(s) / 1000)
    except:
        pass
    return None
