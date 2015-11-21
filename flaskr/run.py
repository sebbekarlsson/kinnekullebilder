from flask import Flask

from flaskr.config import config
from flaskr.views.index import index
from flaskr.views.register import register
from flaskr.models import initialize_database


app = Flask(__name__)
app.register_blueprint(index)
app.register_blueprint(register)

def run():
    initialize_database()
    app.run(
        debug=config['flaskr']['debug'],
        host=config['flaskr']['host'],
    )