from app import db

class Topic(db.Model):
    __tablename__ = 'topics'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    slug = db.Column(db.String(255), unique=True, nullable=False)
    title = db.Column(db.String(255), unique=True, nullable=False)
    author_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), nullable=False)
    entries_count = db.Column(db.BigInteger, default=0, nullable=False)
    is_deleted = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())

    author = db.relationship("User", backref=db.backref("topics", lazy="dynamic"), lazy="selectin")
    entries = db.relationship("Entry", backref="topic", lazy='dynamic')