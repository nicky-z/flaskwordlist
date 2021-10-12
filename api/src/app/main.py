from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app, resources={r'*': {'origin': '*' }})

api = Api(app)

from views.routes import AddWord

api.add_resource(AddWord,'/word/add')

if __name__== '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)