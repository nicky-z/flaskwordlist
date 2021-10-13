
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

WORDS = {
    'word1': {'word':'apple'},
    'word2': {'word':'banana'},
    'word3': {'word':'orange'},
}


def abort_if_word_doesnt_exist(word_id):
    if word_id not in WORDS:
        abort(404, message="Word {} doesn't exist".format(word_id))

parser = reqparse.RequestParser()
parser.add_argument('word')


# # Todo
# # shows a single todo item and lets you delete a todo item
# class Todo(Resource):
#     def get(self, todo_id):
#         abort_if_todo_doesnt_exist(todo_id)
#         return TODOS[todo_id]

#     def delete(self, todo_id):
#         abort_if_todo_doesnt_exist(todo_id)
#         del TODOS[todo_id]
#         return '', 204

#     def put(self, todo_id):
#         args = parser.parse_args()
#         task = {'task': args['task']}
#         TODOS[todo_id] = task
#         return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class WordList(Resource):
    def get(self):
        return WORDS

    def post(self):
        args = parser.parse_args()
        word_id = int(max(WORDS.keys()).lstrip('word')) + 1
        word_id = 'word%i' % word_id
        WORDS[word_id] = {'word': args['word']}
        return WORDS[word_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(WordList, '/words')
# api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)

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
