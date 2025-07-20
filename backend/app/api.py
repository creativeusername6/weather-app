from fastapi import APIRouter, Query
from app.weather_service import get_weather_data

router = APIRouter()


@router.get("/weather")
async def get_weather(city: str = Query(..., description="City name, e.g. 'London'")):
    data = await get_weather_data(city)
    return data
