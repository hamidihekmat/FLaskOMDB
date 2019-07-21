#!/usr/bin/env3 python3

import requests


def getMovie(movie):
    '''takes movie name and returns a json files of all matching movies from the omdb api'''
    url = 'http://www.omdbapi.com/?s=%s&apikey=636b942b' % movie
    response = requests.get(url)
    searchData = response.json()
    return searchData
