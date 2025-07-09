from select import select
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.seller import SellerCreate
from app.database.models import Seller
from passlib.context import CryptContext


password_context = CryptContext(schemes=["bcrypt"])


class SellerService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, credentials: SellerCreate) -> Seller:
        seller = Seller(
            **credentials.model_dump(exclude=["password"]),
            # Hashed password
            password_hash=password_context.hash(credentials.password),
        )
        self.session.add(seller)
        await self.session.commit()
        self.session.refresh(seller)

        return seller



    async def token(self , email , password)->str:
        #validate the credentials
        result = await self.session.execute(select(Seller).where(Seller.email == email))
        seller = result.scalar()
        if seller is None or password_context.verify(
            password,
            seller.password_hash
        ):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Email or password is  incorrect")
        
        