from flask import Flask

from flaskr.config import config

from flaskr.views.index import index
from flaskr.views.register import register
from flaskr.views.login import login
from flaskr.views.logout import logout
from flaskr.views.forum import forum
from flaskr.views.forum_upload import forum_upload
from flaskr.views.forum_places import forum_places
from flaskr.views.forum_images import forum_images
from flaskr.views.forum_profile import forum_profile

from flaskr.models import initialize_database

from flaskr.api.functions import get_notification_action


app = Flask(__name__)

app.jinja_env.globals.update(get_notification_action=get_notification_action)

app.register_blueprint(index)
app.register_blueprint(register)
app.register_blueprint(login)
app.register_blueprint(logout)
app.register_blueprint(forum)
app.register_blueprint(forum_upload)
app.register_blueprint(forum_places)
app.register_blueprint(forum_images)
app.register_blueprint(forum_profile)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
