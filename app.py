import os
from flask import Flask
from flask_restful import Api
from resources.krupasindhu import krupasindhuData

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('mysql://KCAL_USR:bapu18112025@localhost/203.192.211.193')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'abhi'
api = Api(app)

api.add_resource(krupasindhuData, '/krupasindhu')

if __name__ == "__main__":
    from db import db

    db.init_app(app)
    app.run(port=5001, debug=True)
