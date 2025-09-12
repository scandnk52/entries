from flask import Blueprint, redirect, url_for, render_template, flash
from flask_login import login_required, current_user

from app.decorators.user import username_match_required, password_verification_required
from app.forms.user import UpdateUsernameForm, UpdateEmailForm, UpdatePasswordForm, UpdateBiographyForm, \
    UpdateAvatarForm
from app.services.entry import get_user_entries_paginated
from app.services.topic import get_user_topics_paginated
from app.services.user import get_user_by_username, update_user_username, update_user_email, update_user_password, \
    update_user_biography, update_user_avatar, reset_user_avatar

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('<username>')
@user_bp.route('<username>/<int:page>')
def profile(username, page = 1):
    user = get_user_by_username(username)

    if user is None:
        return redirect(url_for('main.home'))

    user_entries = get_user_entries_paginated(user, page)
    return render_template('user/entries.html', user=user, entries=user_entries)


@user_bp.route('/<username>/topics/')
@user_bp.route('/<username>/topics/<int:page>')
def get_topics(username, page = 1):
    user = get_user_by_username(username)

    if user is None:
        return redirect(url_for('main.home'))

    user_topics = get_user_topics_paginated(user, page)
    return render_template('user/topics.html', user=user, topics=user_topics)

@user_bp.route('/<username>/settings/')
@login_required
@username_match_required
def settings(username):
    return redirect(url_for('user.update_biography', username=username))

@user_bp.route('/<username>/settings/username', methods=['GET', 'POST'])
@login_required
@username_match_required
@password_verification_required('current_password')
def update_username(username):
    form = UpdateUsernameForm()
    if form.validate_on_submit():
        username = form.username.data
        if update_user_username(current_user, username):
            flash("Username updated successfully", 'success')
        else:
            flash("Username could not be updated", 'error')
        return redirect(url_for('user.update_username', username=username))

    return render_template('user/settings/username.html', form=form, user=current_user)

@user_bp.route('/<username>/settings/email', methods=['GET', 'POST'])
@login_required
@username_match_required
@password_verification_required('current_password')
def update_email(username):
    form = UpdateEmailForm()
    if form.validate_on_submit():
        email = form.email.data
        if update_user_email(current_user, email):
            flash("Email updated successfully", 'success')
        else:
            flash("Email could not be updated", 'error')
        return redirect(url_for('user.update_email', username=username))

    return render_template('user/settings/email.html', form=form, user=current_user)

@user_bp.route('/<username>/settings/password', methods=['GET', 'POST'])
@login_required
@username_match_required
@password_verification_required('current_password')
def update_password(username):
    form = UpdatePasswordForm()
    if form.validate_on_submit():
        password = form.password.data
        if update_user_password(current_user, password):
            flash("Password updated successfully", 'success')
        else:
            flash("Password could not be updated", 'error')
        return redirect(url_for('user.update_password', username=username))

    return render_template('user/settings/password.html', form=form, user=current_user)

@user_bp.route('/<username>/settings/biography', methods=['GET', 'POST'])
@login_required
@username_match_required
def update_biography(username):
    form = UpdateBiographyForm(biography=current_user.biography)
    if form.validate_on_submit():
        biography = form.biography.data
        if update_user_biography(current_user, biography):
            flash("Biography updated successfully", 'success')
        else:
            flash("Biography could not be updated", 'error')
        return redirect(url_for('user.update_biography', username=username))

    return render_template('user/settings/biography.html', form=form, user=current_user)

@user_bp.route('/<username>/settings/avatar', methods=['GET', 'POST'])
@login_required
@username_match_required
def update_avatar(username):
    form = UpdateAvatarForm()
    if form.validate_on_submit():
        avatar_file = form.avatar.data
        if update_user_avatar(current_user, avatar_file):
            flash("Avatar updated successfully", 'success')
        else:
            flash("Avatar could not be updated", 'error')
        return redirect(url_for('user.update_avatar', username=username))

    return render_template('user/settings/avatar.html', form=form, user=current_user)

@user_bp.route('/<username>/reset/avatar', methods=['POST'])
@login_required
@username_match_required
def reset_avatar(username):
    if reset_user_avatar(current_user):
        flash("Avatar reset successfully", 'success')
    else:
        flash("Avatar could not be reset", 'warning')
    return redirect(url_for('user.update_avatar', username=username))