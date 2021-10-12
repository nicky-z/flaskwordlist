from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class WordList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.Text, nullable=False)

