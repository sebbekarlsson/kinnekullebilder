from flask import Blueprint, render_template, abort, request, redirect
from flaskr.api.functions import get_current_user

from flaskr.models import sess, Image, User, Place, Comment


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


    return render_template('forum_images.html', current_user=current_user, images=images)


@forum_images.route('/forum/images/image/<image_id>', methods=['POST','GET'])
def _forum_images_image(image_id):
    current_user = get_current_user()

    if current_user is None:
        return redirect('/')

    comments = None

    image = sess.query(Image).filter(Image.id==image_id).first()

    if image is not None:
        comments = sess.query(Comment).filter(Comment.id==image.id).all()
        uploader = sess.query(User).filter(User.id==image.user_id).first()

    return render_template('forum_image.html', current_user=current_user, image=image, comments=comments, uploader=uploader)