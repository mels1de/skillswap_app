import asyncio
import asyncpg
from app.core.config import settings

async def main():
    admin_url = (
        str(settings.database_url)
        .replace("/skill_swap_db", "/postgres")
        .replace("+asyncpg", "")
    )
    conn = await asyncpg.connect(dsn=admin_url)

    await conn.execute("""
        SELECT pg_terminate_backend(pid)
        FROM pg_stat_activity
        WHERE datname = 'skill_swap_db'
          AND pid <> pg_backend_pid();
    """)


    await conn.execute("DROP DATABASE IF EXISTS skill_swap_db;")
    await conn.execute("""
        CREATE DATABASE skill_swap_db
        WITH ENCODING 'UTF8'
        LC_COLLATE='en_US.UTF-8'
        LC_CTYPE='en_US.UTF-8'
        TEMPLATE template0;
    """)
    await conn.close()
    print("Database dropped and recreated in UTF8.")

if __name__ == "__main__":
    asyncio.run(main())
