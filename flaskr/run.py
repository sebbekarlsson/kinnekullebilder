from flask import Flask

from flaskr.config import config

from flaskr.views.index import index
from flaskr.views.register import register
from flaskr.views.login import login
from flaskr.views.logout import logout

from flaskr.models import initialize_database


app = Flask(__name__)

app.register_blueprint(index)
app.register_blueprint(register)
app.register_blueprint(login)
app.register_blueprint(logout)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


def run():
    initialize_database()
    app.run(
        debug=config['flaskr']['debug'],
        host=config['flaskr']['host']
    )