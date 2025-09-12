from app import db

class Entry(db.Model):
    __tablename__ = 'entries'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    topic_id = db.Column(db.BigInteger, db.ForeignKey("topics.id"), nullable=False, index=True)
    author_id = db.Column(db.BigInteger, db.ForeignKey("users.id"), nullable=False, index=True)
    content = db.Column(db.Text, nullable=False)
    is_deleted = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())
    
    author = db.relationship("User", backref=db.backref("entries", lazy="dynamic"), lazy="selectin")