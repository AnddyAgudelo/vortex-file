from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from api.router_api import routers_api
from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application starting...")
    env = settings.ENV
    app.mongodb_client = AsyncIOMotorClient(settings.DB_CONNECTION)
    app.database = app.mongodb_client[settings.DB_NAME]
    print(f"Started successfully: {env.value}")

    yield
    print("Application closing...")
    app.mongodb_client.close()


app = FastAPI(lifespan=lifespan)

for router in routers_api:
    app.include_router(router, prefix=f"{settings.API_STR}{router.prefix}")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
