from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Quotes(Resource):
    def get(self):
        return {
            'bad': {
                'quotes': [
                    'fuck you',
                    'eat shit'
                ]
            },
            'good': {
                'quotes': [
                    'you are great!',
                    'keep it up!'
                ]
            }
        }

api.add_resource(Quotes, '/end')

if __name__ == '__main__':
    app.run(debug=True)