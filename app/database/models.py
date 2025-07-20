from datetime import datetime
from enum import Enum
from uuid import uuid4, UUID
from pydantic import EmailStr
from sqlmodel import Column, Field, Relationship, SQLModel
from sqlalchemy.dialects import postgresql

class ShipmentStatus(str, Enum):
    placed = "placed"
    in_transit = "in_transit"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered"


class Shipment(SQLModel, table=True):
    __tablename__ = "shipment"

    id: UUID = Field(sa_column=Column(
        postgresql.UUID,
        default = uuid4, 
        primary_key = True)
                     )
    content: str
    weight: float = Field(le=25)
    destination: int
    status: ShipmentStatus
    estimated_delivery: datetime
    seller_id: UUID = Field(foreign_key="seller.id")
    seller: "Seller" = Relationship(back_populates="shipments", sa_relationship_kwargs={
                                    "lazy": "selection"})  # This will relate seller with shipment using the foreign key


class Seller(SQLModel, table=True):
    id: UUID = Field(sa_column=Column(
        postgresql.UUID,
        default=uuid4,
        primary_key=True)
    )
    name: str
    email: EmailStr
    password_hash: str

    Shipments: list[Shipment] = Relationship(back_populates="seller",
                                             sa_relationship_kwargs={"lazy": "selection"})
