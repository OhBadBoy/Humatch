from sqlalchemy.dialects.mysql import INTEGER as MyInteger
from ..database import db
class Person(db.Model):
    __tablename__ = "people"
    id = db.Column(MyInteger(unsigned=True), primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    phone = db.Column(db.String(40))
    password_hash = db.Column(db.String(255))
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.TIMESTAMP, server_default=db.text("CURRENT_TIMESTAMP"))
    advertisements_created = db.relationship("Advertisement", back_populates="creator")
    applications = db.relationship("Application", back_populates="person")
