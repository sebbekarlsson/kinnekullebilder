from flask import Blueprint, render_template, abort, request
from flaskr.api.functions import get_current_user, get_random_string
from flaskr.forms import Upload_image_form
from werkzeug import secure_filename

from flaskr.models import sess, Image, User, Place


forum_upload = Blueprint('forum_upload', __name__,
                        template_folder='templates')

@forum_upload.route('/forum/upload', methods=['POST','GET'])
def _forum_upload():
    current_user = get_current_user()

    form = Upload_image_form(csrf_enabled=False)

    msg = None

    if form.validate_on_submit():
        title = form.title.data
        description = form.title.description
        place = form.place.data

        old_place = sess.query(Place).filter(Place.name==place).first()

        if old_place is None:
            new_place = Place(
                name=place
            )
            sess.add(new_place)
            sess.commit()
        else:
            new_place = old_place

        new_filename = get_random_string(16) + '.' + form.image.data.filename.split('.')[1]

        old_image = sess.query(Image).filter(Image.filename==new_filename).first()

        while old_image is not None:
            new_filename = get_random_string(16) + '.' + form.image.data.filename.split('.')[1]
            old_image = sess.query(Image).filter(Image.filename==new_filename).first()

        image = Image(
            filename=new_filename,
            place_id=new_place.id,
            user_id=current_user.id,
            title=title,
            description=description
        )

        sess.add(image)
        sess.commit()

        form.image.data.save('flaskr/static/upload/image/' + new_filename)

        msg = 'Din bild var uppladdad!'

    return render_template('forum_upload.html', current_user=current_user, form=form, msg=msg)