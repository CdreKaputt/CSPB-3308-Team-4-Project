from flask import request, jsonify
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)
from werkzeug.security import generate_password_hash, check_password_hash
from app.api.auth import bp
from app.extensions import db
from app.models import User


@bp.route("/signup", methods=["POST"])
def register():
    data = request.get_json(silent=True)    # silent=True prevents default 415 res

    if not data:
        return jsonify({"error": "No data provided"}), 400

    if not all(
        k in data for k in ("username", "email", "password", "first_name", "last_name")
    ):
        return jsonify({"error": "Missing required fields"}), 400

    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"error": "Username already taken"}), 409

    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "Email already registered"}), 409

    user = User(
        username=data["username"],
        email=data["email"],
        first_name=data["first_name"],
        last_name=data["last_name"],
        password_digest=generate_password_hash(data["password"]),
    )

    try:
        db.session.add(user)
        db.session.commit()
    except Exception:
        db.session.rollback()  # Ensures that partial commits are cleared
        return jsonify({"error": "Could not create user"}), 500

    return jsonify({"message": "User created successfully"}), 201


@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    if not all(k in data for k in ("username", "password")):
        return jsonify({"error": "Missing required fields"}), 400

    user = User.query.filter_by(username=data["username"]).first()

    if not user or not check_password_hash(user.password_digest, data["password"]):
        return jsonify({"error": "Invalid username or password"}), 401

    access_token = create_access_token(identity=str(user.id))
    refresh_token = create_refresh_token(identity=str(user.id))

    return jsonify({
        "access_token": access_token,
        "refresh_token": refresh_token,
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        },
    }), 200


@bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify({"access_token": access_token}), 200


@bp.route("/logout", methods=["DELETE"])
@jwt_required()
def logout():
    # No server-side session to destroy — the frontend discards the token.
    # TODO: add a token blocklist (DB or Redis) to invalidate tokens on logout.
    return jsonify({"message": "Successfully logged out"}), 200
