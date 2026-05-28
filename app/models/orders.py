from pydantic import BaseModel, Field, EmailStr

class Order(BaseModel):
        order_id: int
        name: str = Field(min_length=3, max_length=60)
        email: EmailStr
        contact: str
        items: list[str]
        total: float = Field(ge=1, le=100)
        location: str
        payment_status: str

        