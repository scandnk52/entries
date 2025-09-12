import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    APP_NAME = os.getenv("APP_NAME")
    APP_VERSION = os.getenv("APP_VERSION")
    APP_PORT = os.getenv("APP_PORT", default="5000")

    SECRET_KEY = os.getenv("SECRET_KEY")

    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'app', 'static', 'uploads')
    AVATAR_FOLDER = os.path.join(UPLOAD_FOLDER, 'avatar')
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024

    PER_PAGE = 10

    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_NAME = os.getenv("DB_NAME")
    DB_PORT = os.getenv("DB_PORT")

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}".format(
        DB_USER,
        DB_PASS,
        DB_HOST,
        DB_PORT,
        DB_NAME,
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False