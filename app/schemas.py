from pydantic import BaseModel , Field

class Shipment (BaseModel):
    content:str = Field(max_length=100)
    weight : float = Field(description="weight of the object" , lt = 25 , ge=1)
    destination:str | None = Field(default=None)