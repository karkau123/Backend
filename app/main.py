
from .schemas import ShipmentRead , ShipmentCreate, ShipmmmentUpdate
from fastapi import FastAPI, status, HTTPException
from scalar_fastapi import get_scalar_api_reference
from typing import Any
app = FastAPI()

shipments = {
    12345: {

        "weight": 0.6,
        "content": "glassware",
        "status": "placed",
    },
    23456: {

        "weight": 1.2,
        "content": "books",
        "status": "in transit",
    },
    34567: {

        "weight": 0.9,
        "content": "electronics",
        "status": "delivered",
    },
    45678: {

        "weight": 2.5,
        "content": "furniture",
        "status": "pending",
    },
    56789: {
        "weight": 0.3,
        "content": "clothing",
        "status": "cancelled",
    },
}


@app.get("/shipment/latest")
def get_latest_shipment() -> dict[str, Any]:
    id = max(shipments.keys())
    return shipments[id]


@app.get("/shipment" , response_model=ShipmentRead)
def get_shipment(id: int | None = None) -> dict[str, Any]:
    if not id:
        id = max(shipments.keys())
        return shipments[id]
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Shipment with id {id} not found"
        )
    return shipments[id]


@app.post("/shipment")
def submit_shipment(shipment : ShipmentCreate) -> dict[str, int]:
    # weight = data.get("weight")
    if shipment.weight > 25:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Weight exceeds the maximum limit of 25kg")
    new_id = max(shipments.keys()) + 1
    shipments[new_id] = {
        "content": shipment.content,
        "weight": shipment.weight,
        "status": "placed",
    }
    return {"id": new_id}


@app.put("/shipment")   # partial data update is not supported , instead use patch method , we usee the put method to update the entire resource while patch is used to update a part of the resource
def shipment_update(id: int, content: str, weight: float, status: str) -> dict[str, Any]:
    shipments[id] = {
        "content": content,
        "weight": weight,
        "status": status,
    }
    return shipments[id]




@app.patch("/shipment")
def update_shipment(
    id: int,
    body:dict[str, ShipmmmentUpdate]
) -> dict[str, Any]:
    shipment = shipments.get(id)
    shipment.update(body)  
    shipments[id] = shipment
    return shipment


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
