from datetime import datetime

from fastapi import APIRouter

health_router = APIRouter()


@health_router.get('/', summary='健康检查')
def get_health_api():
    return {'current_time': str(datetime.now())}
