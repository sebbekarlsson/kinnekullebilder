from flask import Flask

from flaskr.config import config

from flaskr.views.index import index


app = Flask(__name__)
app.register_blueprint(index)

def run():
    app.run(
        debug=config['flaskr']['debug'],
        host=config['flaskr']['host']
    )