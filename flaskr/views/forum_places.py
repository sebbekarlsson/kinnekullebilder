from flask import Blueprint, render_template, abort, request, redirect
from flaskr.api.functions import get_current_user

from flaskr.models import sess, Image, User, Place


forum_places = Blueprint('forum_places', __name__,
                        template_folder='templates')

@forum_places.route('/forum/places', methods=['POST','GET'])
def _forum_places():
    current_user = get_current_user()

    if current_user is None:
        return redirect('/')

    places = sess.query(Place).order_by(Place.created.desc()).all()

    return render_template('forum_places.html', current_user=current_user, places=places)