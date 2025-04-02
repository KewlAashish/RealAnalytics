from . import db
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.dialects.postgresql import JSON

class ArticleAnalytics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.String(100), unique=True, nullable=False)
    clicks = db.Column(db.Integer, default=0)
    time_spent = db.Column(db.Float, default=0.0)
    browser_counts = db.Column(MutableDict.as_mutable(JSON), default=dict)
    os_counts = db.Column(MutableDict.as_mutable(JSON), default=dict)
