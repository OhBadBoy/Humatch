from flask import Blueprint, request, jsonify
from ..database import db
from ..models.company import Company
companies_bp = Blueprint("companies", __name__, url_prefix="/companies")
@companies_bp.get("")
def list_companies():
    rows = Company.query.order_by(Company.created_at.desc()).all()
    return jsonify([{"id":c.id,"name":c.name,"sector":c.sector,"description":c.description,"contact_email":c.contact_email,"phone":c.phone,"website":c.website} for c in rows])
@companies_bp.post("")
def create_company():
    d = request.get_json() or {}
    c = Company(name=d["name"], sector=d.get("sector"), description=d.get("description"), contact_email=d.get("contact_email"), phone=d.get("phone"), website=d.get("website"))
    db.session.add(c); db.session.commit()
    return jsonify({"id": c.id}), 201
@companies_bp.get("/<int:company_id>")
def get_company(company_id):
    c = Company.query.get_or_404(company_id)
    return jsonify({"id":c.id,"name":c.name,"sector":c.sector,"description":c.description,"contact_email":c.contact_email,"phone":c.phone,"website":c.website})
@companies_bp.put("/<int:company_id>")
def update_company(company_id):
    c = Company.query.get_or_404(company_id)
    d = request.get_json() or {}
    for k in ("name","sector","description","contact_email","phone","website"):
        if k in d: setattr(c,k,d[k])
    db.session.commit()
    return jsonify({"ok":True})
@companies_bp.delete("/<int:company_id>")
def delete_company(company_id):
    c = Company.query.get_or_404(company_id)
    db.session.delete(c); db.session.commit()
    return jsonify({"ok":True})
