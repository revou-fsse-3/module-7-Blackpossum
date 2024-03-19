from flask import Blueprint, render_template,request,jsonify
from connectors.mysql_connector import Session
from models.product import Product
from sqlalchemy import select,func,or_

from flask_login import current_user, login_required
from decorators.role_checker import role_required

from validation.product_schema import product_schema
from cerberus import Validator
from flask_jwt_extended import jwt_required, get_jwt


product_routes = Blueprint('product_routes',__name__)

#  show list of product 
@product_routes.route("/product", methods=['GET'])
@login_required
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

    response_data['name'] = current_user.name
    return render_template("products/product_home.html",response_data=response_data)


# added new product in database
@product_routes.route("/product", methods=['POST'])
@role_required('Admin')
def product_insert():

    v= Validator(product_schema)
    json_data = request.get_json()

    if not v.validate(json_data):
        return jsonify({"error": v.errors}),400

    new_product = Product(
        name=json_data['name'],
        price=json_data['price'],
        description=json_data['description'],
        created_at=func.now()
        )
    session =Session()
    session.begin()

    try:
        session.add(new_product)
        session.commit()
        print(new_product)
    except Exception as e:
        # operation failed
        session.rollback()
        print('Transaction rolled back')
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

@product_routes.route("/product/<id>", methods=['PUT'])
@jwt_required
def product_edit(id):
    session = Session()
    session.begin()
    try:
        product = session.query(Product).fillter(Product.id == id).first()

        product.name = request.form['name']
        product.price = request.form['price']
        product.description = request.form['description']
    except Exception as e:
        session.rollback()
        print(e)
        return {"message" : "product failed to edit, please check console"}
    return {"message" : "succes editing data"}