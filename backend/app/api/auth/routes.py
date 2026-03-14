from flask import request, jsonify, flash, redirect, url_for, session
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)
from werkzeug.security import check_password_hash
from app.api.auth import bp
from app.models import User
from app.middleware.auth import guest_required


@bp.route("/login", methods=["POST"])
@guest_required
def login():
    # data = request.get_json(silent=True)  # silent=True prevents default 415 res
    
    username = request.form.get("username")
    password = request.form.get("password")
    
    data = {
        "username": username,
        "password": password
    }
    
    # if not data:
    #     # return jsonify({"error": "No data provided"}), 400
    #     flash("No data provided", "error")
    #     return redirect(url_for("auth_forms.login"))
        

    # if not all(k in data for k in ("username", "password")):
    #     # return jsonify({"error": "Missing required fields"}), 400
    #     flash("Missing required fields", "error")
    #     return redirect(url_for("auth_forms.login"))

    user = User.query.filter_by(username=data["username"]).first()

    if not user or not check_password_hash(user.password_digest, data["password"]):
        # return jsonify({"error": "Invalid username or password"}), 401
        flash("Invalid username or password", "error")
        return redirect(url_for("auth_forms.login"))       
    else:
        # access_token = create_access_token(identity=str(user.id))
        # refresh_token = create_refresh_token(identity=str(user.id))
        session["user"] = user.username
        # session["access_token"] = access_token
        # session["refresh_token"] = refresh_token
        # flash(f"Welcome back, {username}!")
        return redirect(url_for("main.dashboard"))



    # return jsonify({
    #     "access_token": access_token,
    #     "refresh_token": refresh_token,
    # }), 200
    
    


# @bp.route("/refresh", methods=["POST"])
# @jwt_required(refresh=True)
# def refresh():
#     identity = get_jwt_identity()
#     access_token = create_access_token(identity=identity)
#     return jsonify({"access_token": access_token}), 200


@bp.route("/logout", methods=["POST"])
# @jwt_required()
def logout():
    # No server-side session to destroy — the frontend discards the token.
    # TODO: add a token blocklist (DB or Redis) to invalidate tokens on logout.
    # return jsonify({"message": "Successfully logged out"}), 200
    session.pop("user", None)
    flash("You have been logged out.")
    return redirect(url_for("auth_forms.login"))
