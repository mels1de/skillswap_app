import sqlalchemy
from sqlalchemy import text
from app.core.config import settings

admin_url = settings.database_url.replace("/skill_swap_db", "/postgres").replace("+asyncpg", "+psycopg2")

engine = sqlalchemy.create_engine(admin_url, isolation_level="AUTOCOMMIT")

with engine.connect() as conn:

    conn.execute(text("DROP DATABASE IF EXISTS skill_swap_db"))

    conn.execute(text("""
        CREATE DATABASE skill_swap_db
        WITH ENCODING 'UTF8'
        LC_COLLATE='en_US.UTF-8'
        LC_CTYPE='en_US.UTF-8'
        TEMPLATE template0
    """))

print("✅ Database dropped and recreated in UTF8.")
