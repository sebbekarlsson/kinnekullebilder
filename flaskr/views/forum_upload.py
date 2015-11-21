from flask import Blueprint, render_template, abort, request
from flaskr.api.functions import get_current_user
from flaskr.forms import Upload_image_form


forum_upload = Blueprint('forum_upload', __name__,
                        template_folder='templates')

@forum_upload.route('/forum/upload')
def _forum_upload():
    current_user = get_current_user()

    form = Upload_image_form(request.form, csrf_enabled=False)

    if form.validate_on_submit():
        pass

    return render_template('forum_upload.html', current_user=current_user, form=form)