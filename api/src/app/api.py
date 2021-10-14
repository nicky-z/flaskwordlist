
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from match import match

app = Flask(__name__)
api = Api(app)

WORDS = {
    'word1': {'word':'apple'},
    'word2': {'word':'banana'},
    'word3': {'word':'orange'},
}

FILTERED = {
    
}

parser = reqparse.RequestParser()
parser.add_argument('word')
parser.add_argument('pattern')


class FilterWord(Resource):
    def get(self):
        args = parser.parse_args()
        pattern=args['pattern']
        print('GET', pattern)
        for id in WORDS:
            word=(WORDS[id]['word'])
            # xyz = match(pattern,word)
            # print('match',pattern,word,xyz)
            if match(pattern,word):
                FILTERED[pattern] = {'word': word}
        return FILTERED



# WordList
# shows a list of all word, and lets you POST to add new words
class WordList(Resource):
    def get(self):
        return WORDS

    def post(self):
        args = parser.parse_args()
        postword = args['word']
        print('Post Route, args', args)
        word_id = int(max(WORDS.keys()).lstrip('word')) + 1
        word_id = 'word%i' % word_id
        WORDS[word_id] = {'word': args['word']}
        return WORDS[word_id], 201
    

    
##
## Actually setup the Api resource routing here
##
api.add_resource(WordList, '/words')
api.add_resource(FilterWord, '/words/filter')


if __name__ == '__main__':
    app.run(debug=False)

#----------------------
# from flask import Flask
# from flask_restful import Api
# from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy


# app = Flask(__name__)
# CORS(app, resources={r'*': {'origin': '*' }})

# api = Api(app)

# from views.routes import AddWord


# api.add_resource(AddWord,'/word/add')


# if __name__== '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)
