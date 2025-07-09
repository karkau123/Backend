from pydantic import BaseModel, EmailStr


class BaseSeller(BaseModel):
    name : str
    email : EmailStr


class SellerCreate(BaseSeller):
    name : str
    email : EmailStr
    password : str
    

class SellerRead(BaseSeller):
    name: str
    email: EmailStr