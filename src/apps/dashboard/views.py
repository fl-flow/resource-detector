from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from src.contrib.consts import templates
from src import settings

dashboard_router = APIRouter()


@dashboard_router.get('/', summary='仪表盘', response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse('dashboard.html', {'request': request})
    # with open(str(settings.TEMPLATES_DIR.joinpath('dashboard.html')), 'r') as f:
    #     return HTMLResponse(content=f.read())
