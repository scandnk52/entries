from flask import Flask

from app.routes.main import main_bp
from app.routes.user import user_bp
from app.routes.auth import auth_bp
from app.routes.topic import topic_bp
from app.routes.entry import entry_bp
from app.routes.search import search_bp
from app.routes.errors import errors_bp

def register_routes(app: Flask):
    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(topic_bp)
    app.register_blueprint(entry_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(errors_bp)