
from flask import Flask
from flask_restful import reqparse, Api, Resource
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
            if match(pattern,word):
                FILTERED[pattern] = {'word': word}
        return FILTERED


class WordList(Resource):
    def get(self):
        return WORDS

    def post(self):
        args = parser.parse_args()
        postword = args['word']
        word_id = int(max(WORDS.keys()).lstrip('word')) + 1
        word_id = 'word%i' % word_id
        WORDS[word_id] = {'word': args['word']}
        return WORDS[word_id], 201
    

api.add_resource(WordList, '/words')
api.add_resource(FilterWord, '/words/filter')


if __name__ == '__main__':
    app.run(debug=False)

