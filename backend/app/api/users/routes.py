from flask import request, jsonify, flash, redirect, render_template, url_for
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
)
from werkzeug.security import generate_password_hash
from app.api.users import bp
from app.extensions import db
from app.models import User
from app.middleware.auth import guest_required


@bp.route("/", methods=["GET"])
@jwt_required()
def get_user():
    current_user_id = int(get_jwt_identity())
    user = User.query.get(current_user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
    }), 200


@bp.route("/", methods=["POST"])
@guest_required
def new_user():
    # data = request.get_json(silent=True)  # silent=True prevents default 415 res

    username = request.form.get("username")
    email = request.form.get("email")
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm_password")  
    
    if (password != confirm_password):
        flash("Passwords do not match!", "error")
        return redirect(url_for("auth_forms.signup"))
    
    data = {
        "username": username,
        "password": password,
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }

    # if not data:
    #     return jsonify({"error": "No data provided"}), 400

    # if not all(
    #     k in data for k in ("username", "email", "password", "first_name", "last_name")
    # ):
    #     return jsonify({"error": "Missing required fields"}), 400

    if User.query.filter_by(username=data["username"]).first():
        # return jsonify({"error": "Username already taken"}), 409
        flash("Username already take.", "error")
        

    if User.query.filter_by(email=data["email"]).first():
        # return jsonify({"error": "Email already registered"}), 409
        flash("Email already registered.", "error")
        

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
        flash("Registration successful! Please login.", "Success")
        return redirect(url_for("auth_forms.login"))
    except Exception:
        db.session.rollback()  # Ensures that partial commits are cleared
        # return jsonify({"error": "Could not create user"}), 500
        flash("Could not create user", "error")
        return redirect(url_for("auth_forms.signup"))

    # return jsonify({"message": "User created successfully"}), 201
