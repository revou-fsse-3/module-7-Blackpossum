from sqlalchemy import create_engine
import os


username = "blackpossum"
password = "58390788_Possum"
host = "127.0.0.1"
database_name = "product_review"

ConnectionString = f'mysql+mysqlconnector://{username}:{password}@{host}/{database_name}'
engine = create_engine(ConnectionString)

connection = engine.connect()

print('succesfuly connect to a database')