from functools import wraps
from flask import redirect, url_for, request, flash
from flask_login import current_user

from app.services.user import verify_user_password


def username_match_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        username = kwargs.get('username')
        if username is None or current_user.username != username:
            return redirect(url_for('user.profile', username=current_user.username))
        return f(*args, **kwargs)
    return decorated_function

def password_verification_required(form_password_field='current_password'):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if request.method == 'POST':
                password = request.form.get(form_password_field)
                if not password or not verify_user_password(current_user, password):
                    flash('Invalid password', 'error')
                    return redirect(request.path)
            return f(*args, **kwargs)
        return decorated_function
    return decorator