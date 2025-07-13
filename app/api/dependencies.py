from typing import Annotated

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import Seller
from app.database.session import get_session
from app.services.seller import SellerService
from app.services.shipment import ShipmentService
from app.core.security import oauth2_scheme
from app.utils import decode_access_token

# Asynchronous database session dep annotation
SessionDep = Annotated[AsyncSession, Depends(get_session)]




# Access token data dep

def get_access_token(token: Annotated[str, Depends(oauth2_scheme)])->dict:
    data = decode_access_token(token)
    if data datais None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Acceess token"
        )
    return 

# logged in seller
async def get_current_seller(token_data: Annotated[dict, Depends(get_access_token)], session: SessionDep):
    return await session.get(Seller , token_data["user"]["id"])
        

# Shipment service dep
def get_shipment_service(session: SessionDep):
    return ShipmentService(session)


# Shipment service dep annotation
ServiceDep = Annotated[
    ShipmentService,
    Depends(get_shipment_service),
]


# Seller Service dependency

def get_seller_service(session: SessionDep):
    return SellerService(session)


SellerDep = Annotated[
    Seller ,
    Depends(get_current_seller)
]

# Seller service dep annotation
SellerServiceDep = Annotated[
    SellerService,
    Depends(get_seller_service),
]


