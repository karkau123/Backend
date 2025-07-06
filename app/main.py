
from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from contextlib import asynccontextmanager
from app.database.session import  create_db_tables
from app.api import router

@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    create_db_tables()
    yield
    print("... Stopped")


app = FastAPI(lifespan=lifespan_handler)


app.include_router(router)




@app.get("/scalar", include_in_schema=False)
def get_scalar():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="scalar-api"
    )


# if i write ressponse_model = None then pydantic will skip the validation of the response model
