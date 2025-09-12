from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required

from app.decorators.auth import logout_required
from app.forms.auth import LoginForm, RegisterForm
from app.services.user import authenticate_user, get_user_by_identifier, create_user

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
@logout_required
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = authenticate_user(form.username.data, form.password.data)

        if user:
            login_user(user)
            flash('You were logged in', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Invalid username or password', 'error')

    return render_template("auth/login.html", form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])
@logout_required
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        if get_user_by_identifier(form.username.data) or get_user_by_identifier(form.email.data):
            flash('User already exists', 'warning')
        else:
            create_user(form.username.data, form.email.data, form.password.data)
            flash('You were registered', 'success')
            return redirect(url_for('auth.login'))

    return render_template("auth/register.html", form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('auth.login'))
