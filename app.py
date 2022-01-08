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
    return render_template('index.html', uri=albums[0].images[0]['uri'])


@app.route('/curl')
def curl():
    response = requests.get(
        'https://api.discogs.com/database/search?artist=Heptones&format=LP&type=master',
        headers={'Authorization: Discogs token=AugrlbeikovAiGkBIqufmThyfiuRkyNboopdSFWD'}
    )
    print('ajajajaja')
    return "Hej"
