from sqlalchemy.dialects.mysql import INTEGER as MyInteger
from ..database import db
class Company(db.Model):
    __tablename__ = "companies"
    id = db.Column(MyInteger(unsigned=True), primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    sector = db.Column(db.String(120))
    description = db.Column(db.Text)
    contact_email = db.Column(db.String(255))
    phone = db.Column(db.String(40))
    website = db.Column(db.String(255))
    created_at = db.Column(db.TIMESTAMP, server_default=db.text("CURRENT_TIMESTAMP"))
    advertisements = db.relationship("Advertisement", back_populates="company", cascade="all,delete-orphan", passive_deletes=True)
