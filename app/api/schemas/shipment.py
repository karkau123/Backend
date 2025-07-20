from datetime import datetime
from pydantic import BaseModel, Field
import uuid  # <-- add this import

from app.database.models import ShipmentStatus


class BaseShipment(BaseModel):
    content: str
    weight: float = Field(le=25)
    destination: int


class ShipmentRead(BaseShipment):
    id: uuid.UUID  # <-- change from SQLAlchemy UUID to Python uuid.UUID
    status: ShipmentStatus
    estimated_delivery: datetime


class ShipmentCreate(BaseShipment):
    pass


class ShipmentUpdate(BaseModel):
    status: ShipmentStatus | None = Field(default=None)
    estimated_delivery: datetime | None = Field(default=None)
