import os.path
import uuid
from flask import current_app
from werkzeug.utils import secure_filename

def is_allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

def upload_avatar(file):
    if not file:
        return None

    if not hasattr(file, 'filename'):
        return None

    if is_allowed_file(file.filename):
        extension = file.filename.rsplit('.', 1)[1].lower()
        filename = f"{uuid.uuid4().hex}.{extension}"
        filename = secure_filename(filename)
        file.save(os.path.join(current_app.config['AVATAR_FOLDER'], filename))
        return filename

    return None

def delete_avatar(filename):
    if filename and filename != 'default.png':
        file_path = os.path.join(current_app.config['AVATAR_FOLDER'], filename)
        if os.path.exists(file_path):
            os.remove(file_path)