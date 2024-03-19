from models.base import Base
# import data type using SQLAlchenmy
from sqlalchemy import Integer,String,DateTime,func
from sqlalchemy.orm import mapped_column,relationship,backref

from flask_login import UserMixin
import bcrypt


# create models for product DB schema 
# reffer to base models

class User(Base, UserMixin):
    __tablename__ = 'user'

    id = mapped_column(Integer,primary_key=True, autoincrement=True)
    email = mapped_column(String(190),nullable=False)
    name = mapped_column(String(190),nullable=False)
    password = mapped_column(String(190),nullable=False)
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    role = mapped_column(String(100), nullable=True)

    def set_password(self, plaintext_password):
        self.password = bcrypt.hashpw(plaintext_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')  # Store the hash as a string

    def check_password(self,password):
        # check password from bcrypt package
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))