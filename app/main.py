import datetime
from app.database.models import  ShipmentStatus
from .schemas import ShipmentCreate, ShipmentUpdate , Shipment
from fastapi import FastAPI, status, HTTPException
from scalar_fastapi import get_scalar_api_reference
from contextlib import asynccontextmanager
from app.database.session import SessionDep, create_db_tables


@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    create_db_tables()
    yield
    print("... Stopped")


app = FastAPI(lifespan=lifespan_handler)

# db = database.Database()

# @app.get("/shipment/latest")
# def get_latest_shipment() -> dict[str, Any]:

#     id = max(shipments.keys())
#     return shipments[id]


@app.get("/shipment", response_model=Shipment)
def get_shipment(id: int, session: SessionDep):

    shipment = session.get(Shipment, id)

    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Shipment with id {id} not found"
       
        )
    return shipment

# uvicorn app.main:app --reload


@app.post("/shipment", response_model=None)
def submit_shipment(shipment: ShipmentCreate,  session: SessionDep) -> dict[str, int]:
    new_shipment = Shipment(
        **shipment.model_dump(),
        status=ShipmentStatus.placed,
        estimated_delivery=datetime.datetime.now() + datetime.timedelta(days=3)
    )
    session.add(new_shipment)
    session.commit()
    session.refresh(new_shipment)
    return {"id": new_shipment.id}


@app.patch("/shipment", response_model=None)
def update_shipment(
    id: int,
    shipment_update: ShipmentUpdate,
    session: SessionDep
):

    update = shipment_update.model_dump(exclude_unset=True)
    if not update:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No Data provided to update"
        )
    shipment = session.get(Shipment, id)
    shipment.sqlmodel_update(
        update
    )
    session.add(shipment)  # <-- Fix: add the instance, not the class
    session.commit()
    session.refresh(shipment)
    return shipment


@app.delete("/shipment")
def delete_shipment(id: int, session: SessionDep) -> dict[str, str]:
    session.delete(
        session.get(Shipment, id)
    )
    session.commit()

    return {"detail": f"Shipment with id #{id} deleted successfully"}


@app.get("/scalar", include_in_schema=False)
def get_scalar():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="scalar-api"
    )


# if i write ressponse_model = None then pydantic will skip the validation of the response model
