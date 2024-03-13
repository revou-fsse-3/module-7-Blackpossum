from flask import Blueprint, render_template,request
from connectors.mysql_connector import Session
from models.product import Product
from sqlalchemy import select,func

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

@product_routes.route("/product", methods=['POST'])
def product_insert():
    new_product = Product(
        name=request.form['name'],
        price=request.form['price'],
        description=request.form['description'],
        created_at=func.now()
        )
    session = Session()
    session.begin()

    try:
        session.add(new_product)
        session.commit()
    except Exception as e:
        # operation failed
        session.rollback()
        print(e)
        return {"message" : "failed to created new_product due to error"}
    # operation succes
    return {"message": "new product succesfully created"}