from flask_restful import Resource

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