from flask import Flask 
from connectors.mysql_connector import engine
# import Env
from dotenv import load_dotenv
import os
# import Db Scheme mdoels to use 
from models.product import Product
# import session maker from SQLAlchemy 
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from controllers.product import product_routes
from controllers.user import user_routes

from flask_login import LoginManager  # Correct
from models.user import User
from flask_jwt_extended import JWTManager


# call the function 
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')

# jwt manager 
jwt= JWTManager(app)


# login manager 
login_manager = LoginManager()
login_manager.init_app(app)

# define user loader for checking user data in database
@login_manager.user_loader
def load_user(user_id):
    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()

    return session.query(User).get(int(user_id))

app.register_blueprint(product_routes)
app.register_blueprint(user_routes)


@app.route("/")
def Running_server():
    # insert using SQL 
    # Session = sessionmaker(connection)
    # with Session() as s:
        # execute sql statement 
        # s.execute(text(" INSERT INTO product (name, price, description, created_at) VALUES ('blood orchid', 250000, 'from borneo rain forrest', '2024-02-07 10:00:00')"))
        # s.commit()


    # insert using Models/SQLAlchemy
    # Newproduct= product(name='Dandelion', price=15000, description='Dandelion Stack miniature,home industry', created_at='2024-02-07 10:00:00')
    # Session = sessionmaker(connection)
    # with Session() as s:
    #     s.add(Newproduct)
    #     s.commit()


    return 'server running at port 5000'