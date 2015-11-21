from flask import Blueprint, render_template, abort, request, session, redirect
from flaskr.forms import Login_form
from flaskr.models import sess, User
from flaskr.api.functions import get_current_user


login = Blueprint('login', __name__,
                        template_folder='templates')

@login.route('/login', methods=['POST', 'GET'])
def _login():
    current_user = get_current_user()

    form = Login_form(request.form, csrf_enabled=False)

    msg = None

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        print(email)

        real_user = sess.query(User).filter(User.email==email).first()

        if real_user is None:
            msg = 'Det finns ingen användare med den här email addressen'
        else:
            if password == real_user.password:
                msg = 'Du är nu inloggad'
                session['user_id'] = real_user.id

                return redirect('/')
            else:
                msg = 'Fel lösenord'

    return render_template('login.html', current_user=current_user, form=form, msg=msg)