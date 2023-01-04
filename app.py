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
IMAGE_URI=""
TITLE=""
ARTIST=""

app = Flask(__name__)

@app.route('/')
def artist():
    ARTIST = request.args.get('artist')
    response = requests.get(
        'https://api.discogs.com/database/search?artist=' + ARTIST + '&type=master&format=LP',
        headers={'Authorization': ('Discogs token=%s' % DISCOGS_TOKEN)}
    )
    number_of_hits = len(response.json()['results'])
    if number_of_hits == 0:
        return render_template('artist-not-found.html', artist=artist)
    random_entry = response.json()['results'][randrange(number_of_hits)]
    IMAGE_URI= random_entry['cover_image']
    TITLE = random_entry['title']
    return render_template('index.html', artist=ARTIST, uri=IMAGE_URI, title=TITLE )


@app.route('/yt')
def artistAndYT():
    ARTIST = request.args.get('artist')
    VIDEOID = request.args.get('title')
    IMAGE_URI = request.args.get('imageUri')
    TITLE = request.args.get('title')
 
    VIDEOID = youtubeid(TITLE)

    return render_template('index.html', artist=ARTIST, uri=IMAGE_URI, title=TITLE, videolink=VIDEOID )



def youtubeid(title):
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    videos = []
    videoid = ""
    youtube = build("youtube", "v3", developerKey=GOOGLE_API_KEY)
    try:

        ### Hämta ut den 1:a träffen på youtube = oftast bästa träffen för aktuell skiva
        search_response = youtube.search().list(q=title, part="id,snippet", maxResults=1).execute()
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                videoid += ("%s" % (search_result["id"]["videoId"]))
        print(videoid)

        ### Ifall man vill ha flera länkar sätt maxResults till mer än 1 ovan och gör något av svaret:
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                videos.append("%s (%s)" % (search_result["snippet"]["title"], search_result["id"]["videoId"]))
        for video in videos:
            print (video)
        ###

    except Exception as e: 
        print(e)    

    return videoid
