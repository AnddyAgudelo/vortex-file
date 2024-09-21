from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from core.config import settings


@asynccontextmanager
async def lifespan(api_app: FastAPI):
    print("Application starting...")
    env = settings.ENV
    if not env:
        raise ValueError("ENV not set")
    if env not in ["DEV", "PROD"]:
        raise ValueError("ENV must be DEV or PROD")

    api_app.mongodb_client = AsyncIOMotorClient(settings.DB_CONNECTION)
    api_app.database = api_app.mongodb_client[settings.DB_NAME]

    yield
    print("Application closing...")
    api_app.mongodb_client.close()


app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
