from fastapi.routing import APIRouter

from api.routes.index import index_routing

routing = APIRouter()

# Register more routes here
routing.include_router(index_routing, tags=["Index Route"])