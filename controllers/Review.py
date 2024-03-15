from flask import Blueprints,render_template,request
from connectors.mysql_connector import Session
from models.Review import Review
from sqlalchemy import select,func

review_routes = Blueprints('review_routes',__name__)

@review_routes.route("/review",methods=['GET'])
def review_home():
    response_data=dict()
