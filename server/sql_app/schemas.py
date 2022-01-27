from pydantic import BaseModel

from server.sql_app.database import Base


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int 
    is_active: bool

    class Config:
        orm_mode = True


class PriceHistoryBase(BaseModel):
    price: float


class PriceHistoryCreate(PriceHistoryBase):
    pass


class PriceHistory(PriceHistoryBase):
    id: int
    company_id: int

    class Config:
        orm_mode = True 


class CompanyBase(BaseModel):
    name: str
    ticker: str 


class CompanyCreate(CompanyBase):
    pass


class Company(CompanyBase):
    id: int
    prices: list[PriceHistory]

    class Config:
        orm_mode = True


class UserPortfolioBase(BaseModel):
    price_history_id: int
    user_id: int
    weight: float

class UserPortfolioCreate(UserPortfolioBase):
    pass


class UserPortfolio(UserPortfolioBase):
    id: int

    class Config:
        orm_mode = True
