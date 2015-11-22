from flask import Blueprint, render_template, abort
from flaskr.api.functions import get_current_user

from flaskr.models import sess, Image, Place


index = Blueprint('index', __name__,
                        template_folder='templates')

@index.route('/')
def _index():
    current_user = get_current_user()

    images = sess.query(Image, Place).join(Place).order_by(Image.created.desc()).limit(32).all()

    return render_template('index.html', current_user=current_user, images=images)