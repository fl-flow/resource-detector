from fastapi import FastAPI

from src.router import api_router


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

    return application


app = get_application()
