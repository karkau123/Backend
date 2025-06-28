
from .schemas import ShipmentRead , ShipmentCreate, ShipmmmentUpdate
from fastapi import FastAPI, status, HTTPException
from scalar_fastapi import get_scalar_api_reference
from typing import Any
from .database import shipments , save
app = FastAPI()

 

@app.get("/shipment/latest")
def get_latest_shipment() -> dict[str, Any]:
    id = max(shipments.keys())
    return shipments[id]


@app.get("/shipment")
def get_shipment(id: int):
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Shipment with id {id} not found"
        )
    return shipments[id]
# uvicorn app.main:app --reload

@app.post("/shipment")
def submit_shipment(shipment : ShipmentCreate) -> dict[str, int]:
    if shipment.weight > 25:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Weight exceeds the maximum limit of 25kg")
    new_id = max(shipments.keys()) + 1
    shipments[new_id] = {
        **shipment.model_dump(),
        "id" : new_id,
        "status": "placed",
    }
    save()
    return {"id": new_id}


@app.patch("/shipment" , response_model=ShipmentRead)
def update_shipment(
    id: int,
    body:dict[str, ShipmmmentUpdate]
) :
    
    shipments[id].update(body.model_dump(exclude_none = True))
   
    return shipments[id]


@app.delete("/shipment")
def delete_shipment(id: int) -> dict[str, str]:
    shipments.pop(id)
    return {"detail": f"Shipment with id #{id} deleted successfully"}
    
    

@app.get("/scalar", include_in_schema=False)
def get_scalar():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="scalar-api"
    )


# if i write ressponse_model = None then pydantic will skip the validation of the response model