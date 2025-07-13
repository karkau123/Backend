from http.client import HTTPException
from fastapi import Depends
from typing_extensions import Annotated
from fastapi.security import OAuth2PasswordBearer  , HTTPBearer

from app.utils import decode_access_token

oauth2_scheme   = OAuth2PasswordBearer(
    tokenUrl="/seller/token"
)

class AccessTokenBearer (HTTPBearer):
    async def __call__(self , request):
        
        auth_credentials =   await super.__call__(request)
        token = auth_credentials.credentials
        
        token_data = decode_access_token(token)
        
        if token_data is None:
            raise HTTPException(
                status_code = 401,
                detail = "Invalid token"
            )


access_token_bearer = AccessTokenBearer()

Annotated[dict,Depends(access_token_bearer)]
