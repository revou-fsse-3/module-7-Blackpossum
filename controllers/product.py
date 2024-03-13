from flask import Blueprint, render_template,request
from connectors.mysql_connector import Session
from models.product import Product
from sqlalchemy import select,func

product_routes = Blueprint('product_routes',__name__)

#  show list of product 
@product_routes.route("/product", methods=['GET'])
def product_home():
    response_data =dict()


    session = Session()

    try :
        product_query = select(Product)

        # add filters for search box query 
        if request.args.get('query') != None:
            search_query = request.args.get('query')
            product_query = product_query.where(Product.name.like(f'%{search_query}%'))

        product = session.execute(product_query)
        product = product.scalars()
        response_data['Products'] = product
        print(Product)
    except Exception as e:
        print(e)
        return "error"


    return render_template("products/product_home.html",response_data=response_data)

# added ne product in database
@product_routes.route("/product", methods=['POST'])
def product_insert():
    new_product = Product(
        name=request.form['name'],
        price=request.form['price'],
        description=request.form['description'],
        created_at=func.now()
        )
    session =Session()
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

# delete a product in database 
@product_routes.route("/product/<id>",methods=['DELETE'])
def product_delete(id):
    session = Session()
    session.begin()
    try:
        product_to_delete = session.query(Product).filter(Product.id==id).first()
        session.delete(product_to_delete)
        session.commit()
    except Exception as e:
        session.rollback()
        print(e)
        return {"message" : "failed to delete product, please check console"}
    
    return {"message" : "product sucessfuly deleted"}