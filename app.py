from random import randrange

import discogs_client
import requests
from flask import Flask, render_template, request

DISCOGS_TOKEN = 'AugrlbeikovAiGkBIqufmThyfiuRkyNboopdSFWD'

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
    image_uri = response.json()['results'][randrange(number_of_hits)]['cover_image']
    return render_template('index.html', artist=artist, uri=image_uri)


@app.route('/curl')
def curl():
    print(request.args.get('user'))
    response = requests.get(
        'https://api.discogs.com/releases/3721310',
        headers={'Authorization': ('Discogs token=%s' % DISCOGS_TOKEN)}
    )
    return render_template('index.html',
                           uri=[image["uri"] for image in response.json()['images'] if image["type"] == "primary"][0])
