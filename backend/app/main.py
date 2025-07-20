from fastapi import FastAPI
from app.api import router
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Weather API",
    description="Fetch current and forecasted weather by city name",
    version="1.0.0"
)

app.include_router(router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
