from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
#to use env in DB connector 

username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
database_name = os.getenv("DB_NAME")

print(username)
print(password)
print(host)
print(database_name)




try:
    ConnectionString = f'mysql+mysqlconnector://{username}:{password}@{host}/{database_name}'
    engine = create_engine(ConnectionString)
    connection = engine.connect()
    Session =sessionmaker(connection)
    print('Successfully connected to the database.')

except Exception as e:
    print('Failed to connect to the database:', e)
