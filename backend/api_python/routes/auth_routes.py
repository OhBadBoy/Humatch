from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from ..database import db
from ..models.person import Person
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
bcrypt = Bcrypt()
@auth_bp.post("/register")
def register():
    d = request.get_json() or {}
    if not all(k in d for k in ("first_name","last_name","email","password")):
        return jsonify({"error":"missing fields"}), 400
    if Person.query.filter_by(email=d["email"]).first():
        return jsonify({"error":"email exists"}), 409
    p = Person(first_name=d["first_name"], last_name=d["last_name"], email=d["email"], phone=d.get("phone"))
    p.password_hash = bcrypt.generate_password_hash(d["password"]).decode()
    db.session.add(p); db.session.commit()
    return jsonify({"id": p.id, "email": p.email}), 201
@auth_bp.post("/login")
def login():
    d = request.get_json() or {}
    u = Person.query.filter_by(email=d.get("email")).first()
    if not u or not u.password_hash or not bcrypt.check_password_hash(u.password_hash, d.get("password","")):
        return jsonify({"error":"invalid credentials"}), 401
    token = create_access_token(identity={"id": u.id, "email": u.email, "is_admin": u.is_admin})
    return jsonify({"access_token": token})
@auth_bp.get("/me")
@jwt_required()
def me():
    return jsonify(get_jwt_identity())
