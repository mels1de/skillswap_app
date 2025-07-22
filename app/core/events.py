# app/core/events.py
from fastapi import FastAPI
from typing import Callable, Sequence, Awaitable

def register_lifespan(
    app: FastAPI,
    startups: Sequence[Callable[[], Awaitable[None]]],
    shutdowns: Sequence[Callable[[], Awaitable[None]]],
) -> None:
    @app.on_event("startup")
    async def _startup_event():
        for fn in startups:
            await fn()

    @app.on_event("shutdown")
    async def _shutdown_event():
        for fn in shutdowns:
            await fn()
