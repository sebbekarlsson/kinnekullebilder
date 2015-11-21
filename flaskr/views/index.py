from flask import Blueprint, render_template, abort
from flaskr.api.functions import get_current_user


index = Blueprint('index', __name__,
                        template_folder='templates')

@index.route('/')
def _index():
    current_user = get_current_user()
    return render_template('index.html', current_user=current_user)