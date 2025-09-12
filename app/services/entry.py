from sqlalchemy import func

from app.models import Entry, Topic, User
from app import db

from app.services.topic import get_topic_by_id
from app.utils.text import content_lowercase

def create_entry(topic_id, author_id, content):
    if get_topic_by_id(topic_id) is None:
        return None

    content = content_lowercase(content)

    entry = Entry(topic_id=topic_id, author_id=author_id, content=content)

    db.session.add(entry)
    db.session.commit()

    return entry

def get_entries_paginated(topic: Topic, page = 1, per_page = 10):
    return topic.entries.order_by(Entry.id.asc()).paginate(page=page, per_page=per_page, error_out=False)

def get_user_entries_paginated(user: User, page = 1, per_page = 10):
    return user.entries.order_by(Entry.created_at.desc()).paginate(page=page, per_page=per_page, error_out=False)

def get_entry_page(entry: Entry, per_page = 10):
    count = entry.topic.entries.filter(Entry.created_at < entry.created_at).count()
    return count // per_page + 1

def get_random_entries(limit = 10):
    random_topics = Topic.query.join(Entry).group_by(Topic.id).order_by(func.random()).limit(limit).all()
    random_entries = []
    for topic in random_topics:
        random_entry = topic.entries.order_by(func.random()).first()
        if random_entry:
            random_entries.append(random_entry)
    return random_entries