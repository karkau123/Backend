

from fastapi import APIRouter
 
from ..schemas import sellerCreate

router = APIRouter(prefix="seller")



@router.post("/signup")
def register_seller(seller: sellerCreate):
    pass
