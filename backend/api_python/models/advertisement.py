from sqlalchemy.dialects.mysql import INTEGER as MyInteger
from ..database import db
class Advertisement(db.Model):
    __tablename__ = "advertisements"
    id = db.Column(MyInteger(unsigned=True), primary_key=True, autoincrement=True)
    company_id = db.Column(MyInteger(unsigned=True), db.ForeignKey("companies.id", ondelete="SET NULL", onupdate="CASCADE"), nullable=True)
    title = db.Column(db.String(255), nullable=False)
    short_description = db.Column(db.String(300), nullable=False)
    full_description = db.Column(db.Text)
    wage = db.Column(db.Numeric(10,2))
    location = db.Column(db.String(150))
    working_time = db.Column(db.String(60))
    published_at = db.Column(db.Date)
    expires_at = db.Column(db.Date)
    created_by = db.Column(MyInteger(unsigned=True), db.ForeignKey("people.id", ondelete="SET NULL", onupdate="CASCADE"), nullable=True)
    company = db.relationship("Company", back_populates="advertisements")
    creator = db.relationship("Person", back_populates="advertisements_created")
    applications = db.relationship("Application", back_populates="advertisement", cascade="all,delete-orphan", passive_deletes=True)
