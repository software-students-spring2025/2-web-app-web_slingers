from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from models.user import User
from urllib.parse import urlsplit

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("urls.dashboard"))  # Redirect if already logged in

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user_data = User.find_by_username(username)

        if user_data and User(user_data["_id"], user_data["username"], user_data["password_hash"]).verify_password(password):
            user = User(user_data["_id"], user_data["username"], user_data["password_hash"])
            login_user(user)  # This should log in the user
            
            print(f"User {user.username} logged in successfully!")  # Debugging log

            # Handle Flask-Login's "next" parameter for proper redirection
            next_page = request.args.get("next")
            if not next_page or urlsplit(next_page).netloc != "":
                next_page = url_for("urls.dashboard")

            return redirect(next_page)

        flash("Invalid username or password", "danger")

    return render_template("login.html")

@auth.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("urls.dashboard"))  # Redirect if already logged in

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            flash("Passwords do not match", "danger")
            return redirect(url_for("auth.register"))

        existing_user = User.find_by_username(username)
        if existing_user:
            flash("Username already exists", "danger")
            return redirect(url_for("auth.register"))

        new_user = User.create_user(username, password)
        if new_user:
            flash("Registration successful! Please log in.", "success")
            return redirect(url_for("auth.login"))
        else:
            flash("Error registering user", "danger")

    return render_template("register.html")

@auth.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form.get("email")

        # Mock validation - check if email exists in the system
        user_data = User.find_by_email(email)  # Assuming the User model has this method

        if user_data:
            flash("A password reset link has been sent to your email.", "success")
        else:
            flash("No account found with that email.", "danger")

        return redirect(url_for("auth.forgot_password"))  # Reload the page to show message

    return render_template("forgot_password.html")

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
