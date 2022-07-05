from fastapi.templating import Jinja2Templates

from src import settings

templates = Jinja2Templates(settings.TEMPLATES_DIR)
