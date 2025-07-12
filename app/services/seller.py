import datetime
from sqlalchemy import select  # FIX: import select from sqlalchemy
from fastapi import HTTPException, status
import jwt
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.seller import SellerCreate
from app.database.models import Seller
from passlib.context import CryptContext
from app.config import security_settings

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

    async def token(self, email, password) -> str:
        # validate the credentials
        result = await self.session.execute(select(Seller).where(Seller.email == email))
        seller = result.scalar()
        if seller is None or not password_context.verify(
            password,
            seller.password_hash
        ):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Email or password is  incorrect")

        token = jwt.encode(
            payload={
                "user": {
                    "name": seller.name,
                    "email": seller.email,
                },
                "exp": datetime.datetime.now() + datetime.timedelta(days=1)
            },
            algorithm=security_settings.JWT_ALGORITHM,
            key=security_settings.JWT_SECRET,
        )
        return token
