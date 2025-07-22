from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.skills import router as skills_router

from app.api import auth
from app.core.config import settings
from app.core.events import register_lifespan
from app.services.redis_client import connect_redis, close_redis
from app.services.mq import connect_mq, close_mq

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_title,
        version=settings.app_version,
        docs_url="/docs",
        openapi_url="/openapi.json",
        redoc_url=None,
        debug=True
    )

    register_lifespan(
        app,
        startups=[connect_redis, connect_mq],
        shutdowns=[close_redis, close_mq],
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(auth.router, prefix="/auth", tags=["auth"])
    app.include_router(skills_router)
    return app


app = create_app()
