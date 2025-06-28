from pydantic import BaseModel
from enum import Enum

class ShipmentStatus(str, Enum):
   
    delivered = "delivered"


class BaseShipment(BaseModel):
    placed = "placed"
    in_transit = "in transit"
    out_for_delivery = "out for delivery"


class ShipmentRead (BaseShipment):
    status:  ShipmentStatus
    
    
class ShipmentCreate(BaseShipment):
    pass
    
    
class ShipmmmentUpdate(BaseModel):
    status:  ShipmentStatus

 