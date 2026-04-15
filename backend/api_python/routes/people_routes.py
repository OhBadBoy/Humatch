from flask import Blueprint, jsonify
from ..models.person import Person
people_bp = Blueprint("people", __name__, url_prefix="/people")
@people_bp.get("")
def list_people():
    rows = Person.query.order_by(Person.id.desc()).all()
    return jsonify([{"id":p.id,"first_name":p.first_name,"last_name":p.last_name,"email":p.email,"phone":p.phone,"is_admin":p.is_admin} for p in rows])
