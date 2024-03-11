from flask import Blueprint, render_template
from connectors.mysql_connector import Session
from models.product import Product
from sqlalchemy import select

product_routes = Blueprint('product_routes',__name__)

@product_routes.route("/product", methods=['GET'])
def product_home():
    response_data =dict()


    session = Session()

    try :
        product_query = select(Product)
        product = session.execute(product_query)
        product = product.scalars()
        response_data['Products'] = product
        print(Product)
    except Exception as e:
        print(e)
        return "error"


    return render_template("products/product_home.html",response_data=response_data)

