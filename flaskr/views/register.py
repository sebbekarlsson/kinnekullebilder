from flask import Blueprint, render_template, abort, request
from flaskr.forms import Register_form
from flaskr.models import sess, User
from flaskr.api.functions import get_current_user


register = Blueprint('register', __name__,
                        template_folder='templates')

@register.route('/register', methods=['POST', 'GET'])
def _register():
    current_user = get_current_user()

    form = Register_form(request.form, csrf_enabled=False)

    msg = None

    if form.validate_on_submit():

        old_user = sess.query(User).filter(User.email==form.email.data).first()

        if old_user is not None:
            msg = 'Det finns redan en användare med den här email addressen!'
        else:
            user = User(
                email=form.email.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                password=form.password.data
            )

            sess.add(user)
            sess.commit()

            msg = 'Välkommen, <a href="/login">logga in</a>'

    return render_template('register.html', current_user=current_user, form=form, msg=msg)