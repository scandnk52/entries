from flask import Blueprint, render_template

from app.services.entry import get_random_entries

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    entries = get_random_entries()
    return render_template("main/home.html", entries=entries)