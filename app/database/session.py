
# from app.schemas import Shipment
from sqlalchemy.ext.asyncio import create_async_engine  , AsyncSession
from sqlmodel import SQLModel 
from sqlalchemy.orm import sessionmaker
from app.config import settings

engine  = create_async_engine(
    url = settings.POSTFRES_URL , # this url will be used to make the connectiion with the database
    echo = True,
)
# our fastapi server and the database must run on different threads
async def create_db_tables():
    async with engine.begin() as connection:
        await connection.run_sync(SQLModel.metadata.create_all)
        



async def get_session():
    async_session = sessionmaker(
        bind = engine,
        class_ = AsyncSession,
        expire_on_commit=False,
    )
    with async_session(bind = engine) as session:
        yield session
        
 
