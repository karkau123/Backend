
from .schemas import   ShipmentCreate, ShipmentUpdate
from fastapi import FastAPI, status, HTTPException
from scalar_fastapi import get_scalar_api_reference
from .database.database import Database
app = FastAPI()

db = Database()

# @app.get("/shipment/latest")
# def get_latest_shipment() -> dict[str, Any]:
    
#     id = max(shipments.keys())
#     return shipments[id]


@app.get("/shipment")
def get_shipment(id: int):
    shipment = db.get(id)
    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Shipment with id {id} not found"
        )
    return shipment
# uvicorn app.main:app --reload

@app.post("/shipment")
def submit_shipment(shipment : ShipmentCreate) -> dict[str, int]:
    new_id = db.create(shipment)
    return {"id": new_id}


@app.patch("/shipment" , response_model=None)
def update_shipment(
    id: int,
    shipment: ShipmentUpdate
) :
    
    shipment = db.update(id , shipment)
   
    return shipment


@app.delete("/shipment")
def delete_shipment(id: int) -> dict[str, str]:
    db.delete(id)
    return {"detail": f"Shipment with id #{id} deleted successfully"}
    
    

@app.get("/scalar", include_in_schema=False)
def get_scalar():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="scalar-api"
    )


# if i write ressponse_model = None then pydantic will skip the validation of the response model