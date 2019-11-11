from flask import Flask, render_template, request, redirect, url_for

# from Code.sentence import get_sentence
# from Code.cleanup import *
# from Code.word_count import histogram_dict
# from Code.sample import sample_weight
# from Code.tokenize import read_file
from Code.dictogram import Dictogram, read_file
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Tweet-Generator')


app = Flask(__name__)

@app.route('/')
def index():
    """returns user to the homepage"""
    word_doc = 'Code/txtdocs/fish.txt'
    words = read_file(word_doc)
    histogram = Dictogram(words)
    sentence = histogram.get_sentence(15)
    return render_template("home.html", tweet=sentence)

if __name__ == "__main__":
    app.run(Debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))