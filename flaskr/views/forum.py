from flask import Blueprint, render_template, abort, redirect
from flaskr.api.functions import get_current_user


forum = Blueprint('forum', __name__,
                        template_folder='templates')

@forum.route('/forum')
def _forum():
    current_user = get_current_user()

    if current_user is None:
        return redirect('/')

    return render_template('forum.html', current_user=current_user)