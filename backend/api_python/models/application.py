from sqlalchemy.dialects.mysql import INTEGER as MyInteger
from ..database import db
class Application(db.Model):
    __tablename__ = "application"
    id = db.Column(MyInteger(unsigned=True), primary_key=True, autoincrement=True)
    advertisement_id = db.Column(MyInteger(unsigned=True), db.ForeignKey("advertisements.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    person_id = db.Column(MyInteger(unsigned=True), db.ForeignKey("people.id", ondelete="SET NULL", onupdate="CASCADE"), nullable=True)
    applicant_name = db.Column(db.String(200), nullable=False)
    applicant_email = db.Column(db.String(255), nullable=False)
    applicant_phone = db.Column(db.String(40))
    message = db.Column(db.Text)
    status = db.Column(db.Enum("received","in_review","rejected","accepted"), nullable=False, default="received")
    created_at = db.Column(db.TIMESTAMP, server_default=db.text("CURRENT_TIMESTAMP"))
    advertisement = db.relationship("Advertisement", back_populates="applications")
    person = db.relationship("Person", back_populates="applications")
