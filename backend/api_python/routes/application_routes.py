from flask import Blueprint, request, jsonify
from ..database import db
from ..models.application import Application
application_bp = Blueprint("application", __name__, url_prefix="/application")
@application_bp.get("")
def list_applications():
    rows = Application.query.order_by(Application.id.desc()).all()
    return jsonify([{"id":a.id,"advertisement_id":a.advertisement_id,"person_id":a.person_id,"applicant_name":a.applicant_name,"applicant_email":a.applicant_email,"applicant_phone":a.applicant_phone,"message":a.message,"status":a.status} for a in rows])
@application_bp.post("")
def create_application():
    d = request.get_json() or {}
    a = Application(advertisement_id=d["advertisement_id"], person_id=d.get("person_id"), applicant_name=d["applicant_name"], applicant_email=d["applicant_email"], applicant_phone=d.get("applicant_phone"), message=d.get("message"), status=d.get("status","received"))
    db.session.add(a); db.session.commit()
    return jsonify({"id": a.id}), 201
@application_bp.put("/<int:app_id>")
def update_application(app_id):
    a = Application.query.get_or_404(app_id)
    d = request.get_json() or {}
    for k in ("advertisement_id","person_id","applicant_name","applicant_email","applicant_phone","message","status"):
        if k in d: setattr(a,k,d[k])
    db.session.commit()
    return jsonify({"ok":True})
@application_bp.delete("/<int:app_id>")
def delete_application(app_id):
    a = Application.query.get_or_404(app_id)
    db.session.delete(a); db.session.commit()
    return jsonify({"ok":True})
