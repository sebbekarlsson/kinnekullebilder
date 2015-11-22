from flask import Blueprint, render_template, abort, request, redirect
from flaskr.api.functions import get_current_user

from flaskr.models import sess, Image, User, Place


forum_profile = Blueprint('forum_profile', __name__,
                        template_folder='templates')

@forum_profile.route('/forum/profile/<user_id>', methods=['POST','GET'])
def _forum_profile(user_id):
    current_user = get_current_user()

    if current_user is None:
        return redirect('/')

    profile_user = sess.query(User).filter(User.id==user_id).first()
    images = sess.query(Image).filter(Image.user_id==profile_user.id).limit(32).all()

    return render_template('forum_profile.html', current_user=current_user, profile_user=profile_user, images=images)