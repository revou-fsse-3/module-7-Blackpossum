from flask import Flask 
from connectors.mysql_connector import connection
# import Env
from dotenv import load_dotenv
# import Db Scheme mdoels to use 
from models.product import product
# import session maker from SQLAlchemy 
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

# call the function 
load_dotenv()

app = Flask(__name__)
print('server is comenching')


@app.route("/")
def Running_server():
    # insert using SQL 
    # Session = sessionmaker(connection)
    # with Session() as s:
        # execute sql statement 
        # s.execute(text(" INSERT INTO product (name, price, description, created_at) VALUES ('blood orchid', 250000, 'from borneo rain forrest', '2024-02-07 10:00:00')"))
        # s.commit()


    # insert using Models/SQLAlchemy
    Newproduct= product(name='Dandelion', price=15000, description='Dandelion Stack miniature,home industry', created_at='2024-02-07 10:00:00')
    Session = sessionmaker(connection)
    with Session() as s:
        s.add(Newproduct)
        s.commit()


    return 'server running at port 5000'