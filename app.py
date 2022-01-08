from random import randrange

import discogs_client
import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    d = discogs_client.Client('ExampleApplication/0.1',
                              user_token="AugrlbeikovAiGkBIqufmThyfiuRkyNboopdSFWD")
    results = d.search(artist='Heptones', type='master', format='LP')
    albums = results.page(1)
    return render_template('index.html', uri=albums[1].images[1]['uri'])


@app.route('/artist')
def artist():
    response = requests.get(
        'https://api.discogs.com/database/search?artist=' + request.args.get('name') + '&type=master&format=LP',
        headers={'Authorization': 'Discogs token=AugrlbeikovAiGkBIqufmThyfiuRkyNboopdSFWD'}
    )
    ix = randrange(len(response.json()['results']))
    return render_template('index.html',
                           uri=response.json()['results'][ix]['cover_image'])


@app.route('/curl')
def curl():
    print(request.args.get('user'))
    response = requests.get(
        'https://api.discogs.com/releases/3721310',
        headers={'Authorization': 'Discogs token=AugrlbeikovAiGkBIqufmThyfiuRkyNboopdSFWD'}
    )
    return render_template('index.html',
                           uri=[image["uri"] for image in response.json()['images'] if image["type"] == "primary"][0])
