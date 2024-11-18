import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

load_dotenv()
DB_URL_CONNECTION = f"postgresql+asyncpg://{os.getenv('USER')}:{os.getenv('PASSWORD')}@" \
                    f"{os.getenv('HOST')}:{os.getenv('PORT')}/{os.getenv('DATABASE')}"

engine = create_async_engine(DB_URL_CONNECTION)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_db():
    async with async_session_maker() as session:
        yield session
