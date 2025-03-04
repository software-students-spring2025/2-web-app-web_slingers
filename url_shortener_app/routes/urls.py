from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
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
    user_urls = URL.get_user_urls(current_user.id).limit(2)
    return render_template("dashboard.html", urls=user_urls)

@urls.route("/shorten", methods=["POST"])
@login_required
def shorten():
    long_url = request.form["long_url"]
    short_url = generate_short_url()
    URL.create_url(current_user.id, long_url, short_url)
    return redirect(url_for("urls.dashboard"))

@urls.route("/delete", methods=["GET"])
@login_required
def delete():
    short_url = request.args.get('short_url')
    next = request.args.get('next')
    URL.delete_url(short_url)
    if next:
        return redirect(next)
    return redirect(url_for("urls.dashboard"))

@urls.route("/favorites", methods=["GET","POST"])
@login_required
def favorites():
    if request.method == "GET":
        favs = URL.get_user_favs(current_user.id)
        favs.sort("short_url", pymongo.ASCENDING")
        return render_template("favorites.html", urls=favs)
    # Toggle favorite
    if request.method == "POST":
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        URL.toggle_favorite(current_user.id, data["short_url"])
        fav = URL.get_fav_status(current_user.id, data["short_url"])
        return jsonify({"success": "favorite added", "fav": fav}), 200


@urls.route("/edit/<short_url>", methods=["GET", "POST"])
@login_required
def edit(short_url):
    if request.method == "GET":
        query = {"user_id": current_user.id, "short_url": short_url}
        url = URL.query(query)
        if not url:
            return redirect(url_for("urls.dashboard"))
        return render_template("edit_url.html", url=url.next())
    if request.method == "POST":
        new_long_url = request.form["long_url"]
        result = URL.update_url(short_url, new_long_url)
        if result.matched_count == 0:
            flash("Update failed", "danger")
        else:
            flash("Update successful", "success")

        return redirect(url_for("urls.dashboard"))

@urls.route("/history", methods=["GET"])
@login_required
def history():
    filter = request.args.get("filter")
    if filter:
        query = {
            "$and": [
                {"user_id": current_user.id},
                {"$or": [
                    {"short_url": {"$regex": filter, "$options": "i"}},
                    {"long_url": {"$regex": filter, "$options": "i"}}
                ]}
            ]
        }
        urls = URL.query(query)
    else:
        urls = URL.get_user_urls(current_user.id)
    return render_template("history.html", urls=urls)

# Given a short url, redirect to the corresponding long url
@urls.route("/s/<short_url>", methods=["GET"])
def s(short_url):
    long_url = URL.short_to_long(short_url)
    if long_url:
        return redirect(long_url)
    return redirect(url_for("urls.dashboard"))