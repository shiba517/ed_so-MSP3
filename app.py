import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
# ------------------- Home page (templates/home.html)
@app.route("/home")
def home():
    all_users = mongo.db.users.find()
    return render_template("home.html", users=all_users)


# ------------------- Register page (templates/register.html)
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        check_user_exists = mongo.db.users.find_one({
            "username": request.form.get("username").lower()
        })

        if check_user_exists:
            return redirect(url_for("register"))

        # New user will now be in the database
        new_user = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(new_user)

        # Creating a cookie for the new user
        session["this_user"] = request.form.get("username")

        # Taking new user to their Profile page
        return redirect(url_for("profile", username=session["this_user"]))

    return render_template("register.html")


# ------------------- Login page (templates/login.html)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        check_user_exists = mongo.db.users.find_one({
            "username": request.form.get("username").lower()
        })

        if check_user_exists:
            # Checking if correct password has been entered
            if check_password_hash(check_user_exists["password"], request.form.get("password")):
                # Correct password was entered
                session["this_user"] = request.form.get("username").lower()
                return redirect(url_for("profile", username=session["this_user"]))

            # Incorrect password was entered
            else:
                redirect(url_for("login"))

        # Incorrect username was entered
        else:
            redirect(url_for("login"))

    return render_template("login.html")


# ------------------- Profile page (templates/profile.html)
@app.route("/profile/<username>")
def profile(username):
    if not session.get("this_user"):
        return redirect(url_for("error401"))

    user_info = mongo.db.users.find_one({
        "username": username
    })

    if session["this_user"]:
        return render_template("profile.html", user=user_info)


# ------------------- Logging out
@app.route("/logout")
def logout():
    session.pop("this_user")
    return redirect(url_for("home"))


# ------------------- Error 401 page (templates/error401.html)
@app.route("/error401")
def error401():
    flash("You do not have access to this page")
    return render_template("error401.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)