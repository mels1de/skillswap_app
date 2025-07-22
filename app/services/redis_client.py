from typing import Optional
import redis.asyncio as aioredis
from app.core.config import settings

redis_client: Optional[aioredis.Redis] = None

async def connect_redis():
    global redis_client
    redis_client = aioredis.from_url(
        str(settings.REDIS_URL),
        decode_responses=True,
    )

async def close_redis():
    global redis_client
    if redis_client:
        await redis_client.close()
        await redis_client.wait_closed()
        redis_client = None
