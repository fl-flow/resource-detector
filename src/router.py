from fastapi import APIRouter

from src.apps.healthz.apis import health_router

api_router = APIRouter()

api_router.include_router(health_router, prefix='/healthz', tags=['health'])
