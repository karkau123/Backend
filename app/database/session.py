from sqlalchemy import create_engine 
from sqlmodel import SQLModel

engine  = create_engine(
    url = "sqlite:///sqlite.db" , # this url will be used to make the connectiion with the database
    echo = True,
    # our fastapi server and the database must run on different threads
    connect_args={"check_same_thread": False}   
)

from .models import Shipment
SQLModel.metadata.create_all(bind = engine)
