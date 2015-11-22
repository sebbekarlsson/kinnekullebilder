from flask import Blueprint, render_template, abort, request, redirect
from flaskr.api.functions import get_current_user

from flaskr.models import sess, Image, User, Place


forum_images = Blueprint('forum_images', __name__,
                        template_folder='templates')

@forum_images.route('/forum/images', methods=['POST','GET'])
def _forum_images():
    current_user = get_current_user()

    if current_user is None:
        return redirect('/')

    images = sess.query(Image, Place).join(Place).order_by(Image.created.desc()).all()

    return render_template('forum_images.html', current_user=current_user, images=images)


@forum_images.route('/forum/images/places/<place>', methods=['POST','GET'])
def _forum_images_places(place):
    current_user = get_current_user()

    if current_user is None:
        return redirect('/')

    images = sess.query(Image, Place).filter(Place.name==place).join(Place).order_by(Image.created.desc()).all()

    print(images)

    return render_template('forum_images.html', current_user=current_user, images=images)