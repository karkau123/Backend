from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession 

from app.api.schemas.shipment import Shipment, ShipmentCreate, ShipmentUpdate
from app.database.models import ShipmentStatus

class ShipmentService:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def get(self , id : int) -> Shipment:
        return await self.session.get(Shipment, id)
    
    
    async def add (self , shipment_create : ShipmentCreate)->Shipment:
        new_shipment = Shipment(
            **shipment_create.model_dump(),
            status=ShipmentStatus.placed,
            estimated_delivery=datetime.datetime.now() + datetime.timedelta(days=3)
        )
        self.session.add(new_shipment)
        await self.session.commit()
        await self.session.refresh(new_shipment)
        return new_shipment
    
    
    
    async def update(self , shipment_update :ShipmentUpdate)->Shipment:
        
        shipment = await self.session.get(Shipment, id)
        shipment.sqlmodel_update(
            shipment_update
        )
        self.session.add(shipment)
        await self.session.commit()
        await self.session.refresh(shipment)
        return shipment
    
    
    
    async def delete (self , id : int )->None:
        await self.session.delete(
            await self.get(Shipment, id)
        )
        await self.session.commit()

        return {"detail": f"Shipment with id #{id} deleted successfully"}
    
        
    
    
        
        
