from app.utils.text import render_entry_content
from app.services.topic import get_popular_topics_24h

def init_globals(app):
    app.jinja_env.globals.update(render_entry_content=render_entry_content)
    app.jinja_env.globals.update(get_popular_topics_24h=get_popular_topics_24h)