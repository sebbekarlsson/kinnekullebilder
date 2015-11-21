from flask import session
from flaskr.models import sess, User


def get_current_user():
    current_user = None

    if 'user_id' in session:
        user_id = session['user_id']
        current_user = sess.query(User).filter(User.id==user_id).first()

    return current_user