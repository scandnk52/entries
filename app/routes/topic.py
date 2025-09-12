from flask import Blueprint, redirect, url_for, flash, render_template
from flask_login import current_user, login_required

from app.forms.entry import EntryForm
from app.forms.topic import TopicForm
from app.services.entry import create_entry, get_entries_paginated
from app.services.topic import create_topic, get_topic_by_slug, get_topic_by_title_slug

topic_bp = Blueprint('topic', __name__, url_prefix='/topic')

@topic_bp.route('/new', methods=['GET', 'POST'])
@login_required
def new_topic():
    form = TopicForm()

    if form.validate_on_submit():
        topic = create_topic(title=form.title.data, author_id=current_user.id) or get_topic_by_title_slug(form.title.data)

        if topic:
            create_entry(topic_id=topic.id, author_id=current_user.id, content=form.content.data)
            flash('Your topic created successfully.', 'success')
            return redirect(url_for('topic.get_topic', topic_slug=topic.slug))

    return render_template('topic/new.html', form=form)


@topic_bp.route('/<topic_slug>')
@topic_bp.route('/<topic_slug>/<int:page>')
def get_topic(topic_slug, page = 1):
    topic = get_topic_by_slug(topic_slug)

    if not topic:
        return redirect(url_for('main.home'))

    entries = get_entries_paginated(topic=topic, page=page)
    return render_template('topic/index.html', topic=topic, entries=entries, form=EntryForm())