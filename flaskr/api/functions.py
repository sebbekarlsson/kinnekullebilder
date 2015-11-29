from flask import session
from flaskr.models import sess, User
import random, string


def get_current_user():
    current_user = None

    if 'user_id' in session:
        user_id = session['user_id']
        current_user = sess.query(User).filter(User.id==user_id).first()

    return current_user


def get_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(length))


def get_notification_action(type):
    types = {
        'comment': 'kommenterat'
    }

    return types[type]
