
from fastapi import APIRouter, HTTPException, status
 
from app.api.dependencies import ServiceDep
from app.database.session import SessionDep
from app.api.schemas.shipment import Shipment, ShipmentCreate, ShipmentUpdate
from app.services.shipment import ShipmentService

router = APIRouter()


@router.get("/shipment", response_model=Shipment)
async def get_shipment(id: int, service: ServiceDep):

    shipment = service.get(id)
    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Shipment with id {id} not found"

        )
    return shipment

# uvicorn router.main:router --reload


@router.post("/shipment")
async def submit_shipment(shipment: ShipmentCreate,  session: SessionDep) -> Shipment:
    
    return await ShipmentService(session).add(shipment)


@router.patch("/shipment", response_model=None)
async def update_shipment(
    id: int,
    shipment_update: ShipmentUpdate,
    session: SessionDep
):
    update = shipment_update.model_dump(exclude_none = False)
    if not update:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid update")
    shipment =  await ShipmentService(session).update(shipment_update)
    return shipment


@router.delete("/shipment")
async def delete_shipment(id: int, session: SessionDep) -> dict[str, str]:
    
    await ShipmentService(session).delete(id)
    return {"detail" : f"Shipment with {id} deleted successfully"}