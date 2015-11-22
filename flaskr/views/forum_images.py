from flask import Blueprint, render_template, abort, request, redirect
from flaskr.api.functions import get_current_user

from flaskr.models import sess, Image, User, Place, Comment

from flaskr.forms import Comment_form


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

    form = Comment_form(csrf_enabled=False)

    if current_user is None:
        return redirect('/')

    comments = []

    image = sess.query(Image).filter(Image.id==image_id).first()

    if image is not None:
        uploader = sess.query(User).filter(User.id==image.user_id).first()

        if request.method == 'POST':
            if 'submit' in request.form:
                if request.form['submit'] == 'Skicka':
                    if form.validate_on_submit():
                        comment_text = form.text.data
                        new_comment = Comment(text=comment_text, image_id=image.id, user_id=current_user.id)
                        sess.add(new_comment)
                        sess.commit()
                        form.text.data = None
                elif request.form['submit'] == 'Förkasta':
                    selected_comment_id = request.form['comment_selected']
                    selected_comment = sess.query(Comment).filter(Comment.id==selected_comment_id).delete()
                    sess.commit()
                


        comments = sess.query(Comment, User).filter(Comment.image_id==image.id).order_by(Comment.created.desc()).join(User).all()

    return render_template('forum_image.html', current_user=current_user, image=image, comments=comments, uploader=uploader, form=form)