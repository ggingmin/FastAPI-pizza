from pydantic import BaseModel

class Pizza(BaseModel):

    name: str = None
    price: int = None
    is_cheese_stuffed: bool = None

    class Config:
        orm_mode = True