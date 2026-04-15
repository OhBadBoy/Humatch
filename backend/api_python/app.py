from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from .config.config import Config
from .database import db
from .routes.auth_routes import auth_bp
from .routes.companies_routes import companies_bp
from .routes.people_routes import people_bp
from .routes.advertisements_routes import advertisements_bp
from .routes.application_routes import application_bp

jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    db.init_app(app)
    jwt.init_app(app)

    # Route de santé de base
    @app.get("/health")
    def health():
        return jsonify({"ok": True})

    # Nouvelle route racine pour éviter le 404
    @app.route('/')
    def home():
        return jsonify({"message": "API Flask opérationnelle 🚀"})

    # Route de test de connexion MySQL
    @app.get("/status")
    def status():
        try:
            db.session.execute("SELECT 1")
            return jsonify({"database": "OK", "api": "Running"})
        except Exception as e:
            return jsonify({"database": f"Error: {str(e)}", "api": "Running"}), 500

    # Enregistrement des Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(companies_bp)
    app.register_blueprint(people_bp)
    app.register_blueprint(advertisements_bp)
    app.register_blueprint(application_bp)

    # Création des tables dans la base de données
    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
