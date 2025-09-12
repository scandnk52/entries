from flask import Blueprint, redirect, url_for

errors_bp = Blueprint('errors', __name__)

@errors_bp.app_errorhandler(404)
def page_not_found(e):
    return redirect(url_for('main.home'))