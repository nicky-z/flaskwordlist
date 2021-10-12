from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

#from match import match


app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.db"
db = SQLAlchemy(app)

class Wordlist (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.Text, nullable=False)

    def __str__(self):
        return f'{self.id}{self.word}'

def wordlist_serializer(wordlist):
    return{
        'id': wordlist.id,
        'word':wordlist.word
    }

@app.route('/api/list', methods=['GET'])
def index():
    return 'helllllo'

if __name__ == '__main__':
    app.run()
