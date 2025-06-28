from pydantic import BaseModel, Field
from enum import Enum
 
class ShipmentStatus(str, Enum):
    placed = "placed"
    shipped = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"
    out_for_delivery = "out for delivery"
    in_transit = "in transit"


class BaseShipment(BaseModel):
    content : str
    weight: float = Field(le=25)
    destination : int


class ShipmentRead (BaseShipment):
    status:  ShipmentStatus
    
    
class ShipmentCreate(BaseShipment):
    pass
    
    
class ShipmmmentUpdate(BaseModel):
    status:  ShipmentStatus

 