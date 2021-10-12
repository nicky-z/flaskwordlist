from flask_restful import reqparse, Resource


parser = reqparse.RequestParser()
parser.add_argument('word')


class AddWord(Resource): 
    """ Endpoint for /word/add """
    
    def post(self): 
        try: 
            args = parser.parse_args()
            word = args['word']
            # TODO: connect to database
            return {
                    'word': word,
                    'id': 1
                    }
        except:
            return {
                    'word':'',
                    'id': None
                    }
        
