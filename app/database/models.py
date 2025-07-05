# import datetime
# from sqlmodel import Field,  SQLModel
from enum import Enum


class ShipmentStatus(str, Enum):
    placed = "placed"
    shipped = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"
    out_for_delivery = "out for delivery"
    in_transit = "in transit"


# class Shipment(SQLModel, table=True):
#     __tablename__ = "shipment"
#     id: int = Field(default=None, primary_key=True)
#     content: str
#     weight: float = Field(le=25)
#     destination: int
#     status: ShipmentStatus
#     estimated_delivery: datetime.datetime
