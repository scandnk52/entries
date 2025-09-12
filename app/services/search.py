from app.models import Topic

def search_topic_paginated(query, page, per_page = 10):
    return Topic.query.filter(Topic.title.ilike(f"%{query}%")).paginate(page=page, per_page=per_page, error_out=False)