# app/services/mq.py
from aio_pika import connect_robust, RobustConnection
from app.core.config import settings

mq_conn: RobustConnection | None = None

async def connect_mq() -> RobustConnection:
    global mq_conn
    mq_conn = await connect_robust(str(settings.RABBITMQ_URL))
    return mq_conn

async def close_mq():
    global mq_conn
    if mq_conn:
        await mq_conn.close()
