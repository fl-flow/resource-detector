from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src import settings
from src.router import api_router, view_router


def get_application() -> FastAPI:
    application = FastAPI(
        title='resource-detector',
        description='',
        version='1.0.0',
        docs_url='/api/docs',
        redoc_url='/api/redocs',
        openapi_url='/api/openapi.json',
    )

    application.include_router(api_router, prefix='/api')
    application.include_router(view_router, prefix='/view')

    application.mount('/static', StaticFiles(directory=settings.STATIC_DIR), name='static')

    return application


app = get_application()
