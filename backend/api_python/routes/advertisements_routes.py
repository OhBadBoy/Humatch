from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..database import db
from ..models.advertisement import Advertisement
advertisements_bp = Blueprint("advertisements", __name__, url_prefix="/advertisements")
@advertisements_bp.get("")
def list_ads():
    rows = Advertisement.query.order_by(Advertisement.id.desc()).all()
    return jsonify([{"id":a.id,"company_id":a.company_id,"title":a.title,"short_description":a.short_description,"full_description":a.full_description,"wage":str(a.wage) if a.wage is not None else None,"location":a.location,"working_time":a.working_time,"published_at":a.published_at.isoformat() if a.published_at else None,"expires_at":a.expires_at.isoformat() if a.expires_at else None,"created_by":a.created_by} for a in rows])
@advertisements_bp.post("")
@jwt_required(optional=True)
def create_ad():
    d = request.get_json() or {}
    me = get_jwt_identity() or {}
    a = Advertisement(company_id=d.get("company_id"), title=d["title"], short_description=d["short_description"], full_description=d.get("full_description"), wage=d.get("wage"), location=d.get("location"), working_time=d.get("working_time"), published_at=d.get("published_at"), expires_at=d.get("expires_at"), created_by=me.get("id"))
    db.session.add(a); db.session.commit()
    return jsonify({"id": a.id}), 201
@advertisements_bp.get("/<int:ad_id>")
def get_ad(ad_id):
    a = Advertisement.query.get_or_404(ad_id)
    return jsonify({"id":a.id,"company_id":a.company_id,"title":a.title,"short_description":a.short_description,"full_description":a.full_description,"wage":str(a.wage) if a.wage is not None else None,"location":a.location,"working_time":a.working_time,"published_at":a.published_at.isoformat() if a.published_at else None,"expires_at":a.expires_at.isoformat() if a.expires_at else None,"created_by":a.created_by})
@advertisements_bp.put("/<int:ad_id>")
def update_ad(ad_id):
    a = Advertisement.query.get_or_404(ad_id)
    d = request.get_json() or {}
    for k in ("company_id","title","short_description","full_description","wage","location","working_time","published_at","expires_at"):
        if k in d: setattr(a,k,d[k])
    db.session.commit()
    return jsonify({"ok":True})
@advertisements_bp.delete("/<int:ad_id>")
def delete_ad(ad_id):
    a = Advertisement.query.get_or_404(ad_id)
    db.session.delete(a); db.session.commit()
    return jsonify({"ok":True})
