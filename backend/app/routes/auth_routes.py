from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from werkzeug.security import check_password_hash, generate_password_hash
from app.extensions import db
from app.models import User
from app.utils.auth import required_logged_out

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
@required_logged_out
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # Look up the user by username in the database
        user = User.query.filter_by(username=username).first()
        # Check the user exists and the password matches the stored hash
        if not user or not check_password_hash(user.password_digest, password):
            flash("Invalid username or password.", "error")
            return render_template("login.html")
        # Store the username in the session to keep the user logged in
        session["user"] = user.username
        return redirect(url_for("main.dashboard"))

    # GET: render the empty login form
    return render_template("login.html")


@auth_bp.route("/signup", methods=["GET", "POST"])
@required_logged_out
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        
        # Check that password and confirm password match
        if password != confirm_password:
            flash("Passwords did not match.", "error")
            return render_template("signup.html")
        # Check that the username and email are not already registered
        if User.query.filter_by(username=username).first():
            flash("Username already taken.", "error")
            return render_template("signup.html")
        if User.query.filter_by(email=email).first():
            flash("Email already registered.", "error")
            return render_template("signup.html")
        # Build the new user object, hashing the password before storing it
        user = User(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password_digest=generate_password_hash(password),
        )
        try:
            db.session.add(user)
            db.session.commit()
            flash("Registration successful! Please login.", "success")
            return redirect(url_for("auth.login"))
        except Exception:
            # Roll back any partial changes if the database write fails
            db.session.rollback()
            flash("Could not create user. Please try again.", "error")
            return render_template("signup.html")

    # GET: render the empty signup form
    return render_template("signup.html")


@auth_bp.route("/logout", methods=["POST"])
def logout():
    # Remove the user from the session to log them out
    session.pop("user", None)
    flash("You have been logged out.", "success")
    return redirect(url_for("auth.login"))
