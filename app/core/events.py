from fastapi import FastAPI
from app.services.redis_client import connect_redis,close_redis
from app.services.mq import connect_mq, close_mq

def register_lifespan(app: FastAPI):
    @app.on_event("startup")
    async def startup():
        await connect_redis()
        await connect_mq()

    @app.on_event("shutdown")
    async def shutdown():
        await close_mq()
        await close_redis()