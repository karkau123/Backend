from pydantic import BaseModel , Field
from enum import Enum

class ShipmentStatus(str, Enum):
    placed = "placed"
    in_transit = "in transit"
    out_for_delivery = "out for delivery"
    delivered = "delivered"



class Shipment (BaseModel):
    content:str = Field(max_length=100 , description="contents of the shipment")
    weight : float = Field(description="weight of the object" , lt = 25)
    destination:str | None = Field(description="destination zipcode" , default=None)
    status:  ShipmentStatus