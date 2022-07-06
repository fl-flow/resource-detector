from fastapi import APIRouter

from src.apps.dashboard.views import dashboard_router
from src.apps.healthz.apis import health_router
from src.apps.process_res_info.apis import process_res_info_router
from src.apps.system_res_info.apis import system_res_info_router

api_router = APIRouter()

api_router.include_router(health_router, prefix='/healthz', tags=['health'])
api_router.include_router(system_res_info_router, prefix='/system_res_info', tags=['system_res_info'])
api_router.include_router(process_res_info_router, prefix='/process_res_info', tags=['process_res_info'])

view_router = APIRouter()

view_router.include_router(dashboard_router, prefix='/dashboard', tags=['dashboard'])
