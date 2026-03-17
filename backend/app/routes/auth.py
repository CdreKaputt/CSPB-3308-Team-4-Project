from flask import Blueprint, render_template, redirect, url_for, flash, session
from werkzeug.security import check_password_hash, generate_password_hash
from app.extensions import db
from app.models import User
from app.utils.auth import required_logged_out
from app.utils.forms import LoginForm, SignupForm

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
@required_logged_out
def login():
    form = LoginForm()

    # POST: validate_on_submit() checks that the request is POST and all form fields pass validation
    if form.validate_on_submit():
        # Look up the user by username in the database
        user = User.query.filter_by(username=form.username.data).first()
        # Check the user exists and the password matches the stored hash
        if not user or not check_password_hash(
            user.password_digest, form.password.data
        ):
            flash("Invalid username or password.", "error")
            return render_template("login.html", form=form)
        # Store the username in the session to keep the user logged in
        session["user"] = user.username
        return redirect(url_for("main.dashboard"))

    # GET: render the empty login form
    return render_template("login.html", form=form)


@auth_bp.route("/signup", methods=["GET", "POST"])
@required_logged_out
def signup():
    form = SignupForm()

    # POST: validate_on_submit() checks that the request is POST and all form fields pass validation
    if form.validate_on_submit():
        # Check that the username and email are not already registered
        if User.query.filter_by(username=form.username.data).first():
            flash("Username already taken.", "error")
            return render_template("signup.html", form=form)
        if User.query.filter_by(email=form.email.data).first():
            flash("Email already registered.", "error")
            return render_template("signup.html", form=form)
        # Build the new user object, hashing the password before storing it
        user = User(
            username=form.username.data,
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            password_digest=generate_password_hash(form.password.data),
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
            return render_template("signup.html", form=form)

    # GET: render the empty signup form
    return render_template("signup.html", form=form)


@auth_bp.route("/logout", methods=["POST"])
def logout():
    # Remove the user from the session to log them out
    session.pop("user", None)
    flash("You have been logged out.", "success")
    return redirect(url_for("auth.login"))
