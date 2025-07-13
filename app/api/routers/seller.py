from fastapi.security import OAuth2PasswordRequestForm
from typing_extensions import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from app.core.security import oauth2_scheme
from app.api.schemas.seller import SellerRead, SellerCreate
from app.utils import decode_access_token

from ..dependencies import SellerServiceDep, SessionDep
# Make sure this import path matches your project structure
from app.database.models import Seller

router = APIRouter(prefix="/seller",  tags=["Seller"])


@router.post("/signup", response_model=SellerRead)
async def register_seller(seller: SellerCreate,
                          service: SellerServiceDep
                          ):
    return await service.add(seller)


# Login the seller

@router.post("/token")
async def login_seller(
    request_form: Annotated[OAuth2PasswordRequestForm, Depends()],
    service: SellerServiceDep
):
    token = await service.token(request_form.username, request_form.password)
    return {"access_token": token, "type": "jwt"}

 