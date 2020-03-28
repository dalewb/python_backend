from flask import Flask
from flask_restful import Resource, Api
from quotes import Quotes

app = Flask(__name__)
api = Api(app)

api.add_resource(Quotes, '/end')

if __name__ == '__main__':
    app.run(debug=True)