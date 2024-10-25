from fastapi.routing import APIRouter
from fastapi import status, HTTPException
from sqlmodel import Session, select

from core.db import engine
from models import Settings

settings_router = APIRouter()


@settings_router.post('/settings', status_code=status.HTTP_201_CREATED)
async def add_settings(data: Settings):
    try:
        with Session(engine) as session:
            session.add(data)
            session.commit()
            session.refresh(data)  # Refresh to get the latest state from the DB (like ID)
        return {"message": "Settings added successfully", "settings": data}

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Something went wrong: {str(e)}")


@settings_router.get("/current/settings", status_code=status.HTTP_200_OK)
async def get_settings():
    with Session(engine) as session:
        statement = select(Settings)
        results = session.exec(statement)
        all_settings = []
        for result in results:
            all_settings.append(result)
    return {"settings": all_settings}
