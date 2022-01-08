import discogs_client
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    d = discogs_client.Client('ExampleApplication/0.1',
                              user_token="AugrlbeikovAiGkBIqufmThyfiuRkyNboopdSFWD")
    results = d.search(artist='Heptones', type='master', format='LP')
    albums = results.page(1)
    return render_template('index.html', uri=albums[1].images[1]['uri'])


@app.route('/curl')
def curl():
    response = requests.get(
        'https://api.discogs.com/releases/3721310',
        headers={'Authorization': 'Discogs token=AugrlbeikovAiGkBIqufmThyfiuRkyNboopdSFWD'}
    )
    return render_template('index.html', uri=[image["uri"] for image in response.json()['images'] if image["type"] == "primary"][0])
