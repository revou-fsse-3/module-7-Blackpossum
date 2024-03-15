from models.base import Base
# import data type using SQLAlchenmy
from sqlalchemy import Integer,String,Text,DateTime,func
from sqlalchemy.orm import mapped_column,relationship,backref

# create models for product DB schema 
# reffer to base models

class User(Base):
    __tablename__ = 'user'

    id = mapped_column(Integer,primary_key=True, autoincrement=True)
    email = mapped_column(String(190),nullable=False)
    name = mapped_column(String(190),nullable=False)
    password = mapped_column(String(190),nullable=False)
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())


