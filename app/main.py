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



@app.get("/shipment")
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




@app.get("/scalar", include_in_schema=False)
def get_scalar():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="scalar-api"
    )
