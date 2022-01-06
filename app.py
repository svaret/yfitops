import discogs_client
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  d = discogs_client.Client('ExampleApplication/0.1',
                            user_token="AugrlbeikovAiGkBIqufmThyfiuRkyNboopdSFWD")
  results = d.search(artist='Heptones', type='master', format='LP')
  first = results.page(1)[0]
  image = first.images[0]
  albums = results.page(1)
  uris = []
  for a in albums:
    uris.append(a.images[0]['uri'])
  return render_template('index.html', posts=uris)
