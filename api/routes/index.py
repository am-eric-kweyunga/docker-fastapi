from fastapi.routing import APIRouter

index_routing = APIRouter()

# Index Route hitting "/" path
@index_routing.get("/")
async def index_route():
    return {"message": "Hitting the index page"}
