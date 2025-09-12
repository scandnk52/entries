from flask import Blueprint, redirect, url_for, flash
from flask_login import login_required, current_user

from app.forms.entry import EntryForm
from app.services.entry import create_entry, get_entry_page
from app.services.topic import get_topic_by_slug

entry_bp = Blueprint('entry', __name__, url_prefix='/entry')

@entry_bp.route('/new/<topic_slug>', methods=['POST'])
@login_required
def new_entry(topic_slug):
    topic = get_topic_by_slug(topic_slug)

    if not topic:
        flash('There is no topic like that.', 'warning')
        return redirect(url_for('main.home'))

    page = 1

    form = EntryForm()
    if form.validate_on_submit():
        entry = create_entry(topic_id=topic.id, author_id=current_user.id, content=form.content.data)
        page = get_entry_page(entry)
        flash('Your entry created successfully.', 'success')

    return redirect(url_for('topic.get_topic', topic_slug=topic_slug, page=page))