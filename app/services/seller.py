from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.seller import SellerCreate
from app.database.models import Seller
from passlib.context import CryptContext


password_context = CryptContext(schemes=["bcrypt"])

class sellerService:
    def __init__(self , session : AsyncSession):  
        self.session = session
        
        
    async def add (self , credentials : SellerCreate)-> Seller:
        seller = Seller(
            **credentials.model_dump(exclude=["password"]),
            # Hashed password
            password_hash=password_context.hash(credentials.password),
        
                    )
        self.seesion.add(seller)
        await self.session.commit()
        self.session.refresh(seller)
        
        return seller
        
        
        
        
        