from flask import Blueprint, render_template, abort, session, redirect
from flaskr.api.functions import get_current_user


logout = Blueprint('logout', __name__,
                        template_folder='templates')

@logout.route('/logout')
def _logout():
    if 'user_id' in session:
        del session['user_id']

    return redirect('/')