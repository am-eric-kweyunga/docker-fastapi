import sentry_sdk
from fastapi import FastAPI
from fastapi.routing import APIRoute

from api.main import routing
from core.config import settings


# generating unique id for every route
def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


if settings.SENTRY_DSN and settings.ENVIRONMENT != "local":
    sentry_sdk.init(dsn=str(settings.SENTRY_DSN), enable_tracing=True)

# creating FastAPI instance
app = FastAPI(
    title=settings.PROJECT_NAME,
    version="0.0.1",
    docs_url=f"{settings.API_V_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
    contact={
        "name": "Eric Kweyunga",
        "url": "https://github.com/am-eric-kweyunga",
        "email": "maverickweyunga@gmail.com"
    }
)

app.include_router(routing, prefix=settings.API_V_STR)
