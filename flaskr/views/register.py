from flask import Blueprint, render_template, abort, request
from flaskr.forms import Register_form
from flaskr.models import sess, User


register = Blueprint('register', __name__,
                        template_folder='templates')

@register.route('/register', methods=['POST', 'GET'])
def _register():
    form = Register_form(request.form, csrf_enabled=False)

    msg = None

    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            password=form.password.data
        )

        sess.add(user)
        sess.commit()

        msg='Välkommen, <a href="/login">logga in</a>'

    return render_template('register.html', form=form, msg=msg)