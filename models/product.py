from models.base import Base
# import data type using SQLAlchenmy
from sqlalchemy import Integer,String,Text,DateTime,func
from sqlalchemy.orm import mapped_column


# create models for product DB schema 
# reffer to base models

class product(Base):
    __tablename__ = 'product'

    id = mapped_column(Integer,primary_key=True, autoincrement=True)
    name = mapped_column(String(100),nullable=False)
    price = mapped_column(Integer)
    description = mapped_column(Text)
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())