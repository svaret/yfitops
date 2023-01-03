from random import randrange

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

import sys
import os
import urllib

import discogs_client
import requests
from flask import Flask, render_template, request

DISCOGS_TOKEN = 'AugrlbeikovAiGkBIqufmThyfiuRkyNboopdSFWD'
GOOGLE_API_KEY = 'AIzaSyBoaF8Iw2iP617qopJSC1N1QtDJiq4_Wk8'
VIDEOID = ""

app = Flask(__name__)


@app.route('/discogs-client')
def index():
    d = discogs_client.Client('ExampleApplication/0.1',
                              user_token=DISCOGS_TOKEN)
    results = d.search(artist='Heptones', type='master', format='LP')
    albums = results.page(1)
    return render_template('index.html', uri=albums[1].images[1]['uri'])


@app.route('/')
def artist():
    artist = request.args.get('artist')
    response = requests.get(
        'https://api.discogs.com/database/search?artist=' + artist + '&type=master&format=LP',
        headers={'Authorization': ('Discogs token=%s' % DISCOGS_TOKEN)}
    )
    number_of_hits = len(response.json()['results'])
    if number_of_hits == 0:
        return render_template('artist-not-found.html', artist=artist)
    random_entry = response.json()['results'][randrange(number_of_hits)]
    image_uri = random_entry['cover_image']
    title = random_entry['title']
    VIDEOID = getYoutubeid(title)
    return render_template('index.html', artist=artist, uri=image_uri, title=title, title_length=len(title), videolink=VIDEOID )


def getYoutubeid(title):
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    videos = []
    videoid =""
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=GOOGLE_API_KEY)
    try:
    ### Hämta ut den 1:a träffen på youtube = oftast bästa träffen för aktuell skiva
        search_response = youtube.search().list(q=title, part="id,snippet", maxResults=1).execute()
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                videoid += ("%s" % (search_result["id"]["videoId"]))
        print (videoid)
    ### Ifall man vill ha flera länkar sätt maxResults till mer än 1 ovan och gör något av svaret:
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
               videos.append("%s (%s)" % (search_result["snippet"]["title"],                                       search_result["id"]["videoId"]))
        for video in videos:
            print (video)
    except Exception as e: print(e)
    return videoid


@app.route('/curl')
def curl():
    print(request.args.get('user'))
    response = requests.get(
        'https://api.discogs.com/releases/3721310',
        headers={'Authorization': ('Discogs token=%s' % DISCOGS_TOKEN)}
    )
    return render_template('index.html',
                           uri=[image["uri"] for image in response.json()['images'] if image["type"] == "primary"][0])
