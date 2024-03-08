from flask import Flask 
from connectors.mysql_connector import connection


app = Flask(__name__)
print('server is comenching')


@app.route("/")
def starting_server():
    return 'server running at port 5000'