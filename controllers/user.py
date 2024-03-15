from flask import Blueprint,render_template,request
from connectors.mysql_connector import Session
from models.product import Product
from sqlalchemy import select,or_

user_routes = Blueprint('user_routes',__name__)

# 
@user_routes.route("/register", methods=['GET'])
def user_register():
    return render_template("users/register.html")

@user_routes.route("/register", methods=['POST'])
def do_registration():
    return "abx"