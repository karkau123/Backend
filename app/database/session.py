from fastapi import Depends
from app.schemas import Shipment
from sqlalchemy import create_engine 
from sqlmodel import SQLModel , Session
from typing import Annotated

engine  = create_engine(
    url = "sqlite:///sqlite.db" , # this url will be used to make the connectiion with the database
    echo = True,
    connect_args={"check_same_thread": False}   
)
# our fastapi server and the database must run on different threads
def create_db_tables():
    SQLModel.metadata.create_all(bind = engine)


# session = Session(
#     bind = engine
# )
# session.get(Shipment , 12345)
# session.add(
#     Shipment(id = 12345)
# )
# session.commit()




def get_session():
    with Session(bind = engine) as session:
        yield session
        
SessionDep = Annotated[Session , Depends(get_session)]
