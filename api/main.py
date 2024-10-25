from fastapi.routing import APIRouter

from api.routes.index import index_routing
from api.routes.settings import settings_router

routing = APIRouter()

# Register more routes here
routing.include_router(index_routing, tags=["Index Route"])
routing.include_router(settings_router, tags=["Settings Route"])