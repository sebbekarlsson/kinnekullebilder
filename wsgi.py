from flaskr.app import app
from flaskr.models import initialize_database
from flaskr.config import config


initialize_database()
application = app
