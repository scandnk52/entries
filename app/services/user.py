from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError

from app.models import User
from app import db, login_manager
from app.utils.uploads import delete_avatar, upload_avatar


def create_user(username, email, password):
    if get_user_by_username(username) or get_user_by_email(email):
        return None

    user = User()

    user.username = username
    user.email = email
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return user

@login_manager.user_loader
def get_user_by_id(user_id):
    return User.query.get(int(user_id))

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def get_user_by_identifier(identifier):
    return User.query.filter(or_(User.username == identifier, User.email == identifier)).first()

def authenticate_user(identifier, password):
    user = get_user_by_identifier(identifier)
    return user if user and user.check_password(password) else None

def verify_user_password(user: User, password):
    if not user:
        return False
    return user.check_password(password)

def update_user_username(user: User, username):
    try:
        user.username = username
        db.session.commit()
        return True
    except IntegrityError:
        db.session.rollback()
        return False

def update_user_email(user: User, email):
    try:
        user.email = email
        db.session.commit()
        return True
    except IntegrityError:
        db.session.rollback()
        return False

def update_user_password(user: User, password):
    user.set_password(password)
    db.session.commit()
    return True

def update_user_biography(user: User, biography):
    user.biography = biography
    db.session.commit()
    return True

def update_user_avatar(user: User, avatar_file):
    if not avatar_file:
        return None

    filename = upload_avatar(avatar_file)
    if filename:
        delete_avatar(user.avatar)
        user.avatar = filename
        db.session.commit()
        return True
    return False

def reset_user_avatar(user: User):
    delete_avatar(user.avatar)
    user.avatar = 'default.png'
    db.session.commit()
    return True