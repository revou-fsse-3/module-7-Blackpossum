from flask import Blueprint,render_template,request,redirect
from connectors.mysql_connector import engine,sessionmaker
from models.user import User
from sqlalchemy import select,or_
from flask_login import login_user, logout_user

user_routes = Blueprint('user_routes',__name__)

# 
@user_routes.route("/register", methods=['GET'])
def user_register():
    return render_template("users/register.html")

@user_routes.route("/register", methods=['POST'])
def do_registration():
        
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    newUser = User(name=name, email=email)
    newUser.set_password(password)

    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()

    session.begin()

    try:
        session.add(newUser)
        session.commit()
    except Exception as e:
        session.rollback()
        return {"message":"user registration failure"},500
    
    return {"message":"user register succesfully,continue to login"},201

@user_routes.route("/login", methods=['GET'])
def user_login():
    return render_template("users/login.html")

@user_routes.route("/login", methods=['POST'])
def do_user_login():
    # establish conncetion session
    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()
    # initialize connection
    session.begin()

    try:
        # find / macthing inputed email on database by query 
        user = session.query(User).filter(User.email==request.form['email']).first()

        # conditinal if email doesnt exist 
        if user is None:
            return{"message":"email not match or doesnt exist"}
        
        # find / macthing inputed password on darabase by query
        if not user.check_password(request.form['password']):
            return {"message":"password not macth or doesnt exist"}
        # if login success, this function will save user data to session and created session_id to pass to browser and saved in browser cookie
        login_user(user, remember=False)
        return redirect('/product')

    except Exception as e:
        print(e)
        return {"message": "Login failure incorect user data"},401

@user_routes.route("/logout", methods=['GET'])
def do_user_logout():
    logout_user()
    return redirect('/login')