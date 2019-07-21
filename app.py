#!/usr/bin/env3 python3

from flask import Flask, render_template, request
import requests
from getmovie import getMovie

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'GET':
        return render_template('movie.html')

    if request.method == 'POST':
        searchMovie = request.form['searchmovies']
        searchData = getMovie(searchMovie)
        return render_template('movie.html', data=searchData)
    return render_template('movie.html')


if __name__ == '__main__':
    app.run(debug=True)
