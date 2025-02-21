from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models.url import URL
import random
import string

urls = Blueprint("urls", __name__)

def generate_short_url():
    return "".join(random.choices(string.ascii_letters + string.digits, k=6))

@urls.route("/")
@login_required
def dashboard():
    user_urls = URL.get_user_urls(current_user.id)
    return render_template("dashboard.html", urls=user_urls)

@urls.route("/shorten", methods=["POST"])
@login_required
def shorten():
    long_url = request.form["long_url"]
    short_url = generate_short_url()
    URL.create_url(current_user.id, long_url, short_url)
    return redirect(url_for("urls.dashboard"))

@urls.route("/delete/<short_url>")
@login_required
def delete(short_url):
    URL.delete_url(short_url)
    return redirect(url_for("urls.dashboard"))

@urls.route("/edit/<short_url>", methods=["GET", "POST"])
@login_required
def edit(short_url):
    if request.method == "POST":
        new_long_url = request.form["long_url"]
        URL.update_url(short_url, new_long_url)
        return redirect(url_for("urls.dashboard"))
    return render_template("edit_url.html", short_url=short_url)
