from datetime import datetime, timedelta, timezone

from sqlalchemy import func

from app.models import Topic, User, Entry
from app import db
from app.utils.text import create_title, create_slug

def create_topic(title, author_id):
    title = create_title(title)
    slug = create_slug(title)

    if get_topic_by_slug(slug) or slug == "new":
        return None

    topic = Topic(slug=slug, title=title, author_id=author_id)

    db.session.add(topic)
    db.session.commit()

    return topic

def get_topic_by_slug(slug):
    return Topic.query.filter_by(slug=slug).first()

def get_topic_by_title_slug(title):
    return Topic.query.filter_by(slug=create_slug(title)).first()

def get_topic_by_id(topic_id):
    return Topic.query.get(topic_id)

def get_user_topics_paginated(user: User, page = 1, per_page = 10):
    return user.topics.order_by(Topic.created_at.desc()).paginate(page=page, per_page=per_page, error_out=False)

def get_popular_topics_24h(limit = 10):
    last_24h = datetime.now(timezone.utc) - timedelta(hours=24)
    return Topic.query.with_entities(
        Topic,
        func.count(Entry.id).label('entry_count')
    ).join(
        Entry
    ).filter(
        Entry.created_at >= last_24h
    ).group_by(
        Topic.id
    ).order_by(
        func.count(Entry.id).desc()
    ).limit(limit).all()