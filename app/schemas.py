import datetime
from sqlmodel import SQLModel, Field
from app.database.models import ShipmentStatus


class BaseShipment(SQLModel):
    content: str
    weight: float = Field(le=25)
    destination: int


class Shipment (BaseShipment, table=True):
    id: int = Field(default=None, primary_key=True)
    status:  ShipmentStatus
    estimated_delivery: datetime.datetime


class ShipmentCreate(BaseShipment):
    pass


class ShipmentUpdate(SQLModel):
    status:  ShipmentStatus | None = Field(default=None)
    estimated_delivery: datetime.datetime | None = Field(default=None)
