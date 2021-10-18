import os
import datetime
import re
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
            "password": generate_password_hash(request.form.get("password")),
            "register_date": datetime.datetime.now().strftime("%B " + "%d " + "%Y")
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


# ------------------- Add recipe page (templates/add_recipe.html)
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        if not session.get("this_user"):
            return redirect(url_for("error401"))

        # New recipe will now be in the database
        new_recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_instructions": request.form.get("recipe_instructions"),
            "created_by": session["this_user"],
            "post_date": datetime.datetime.now().strftime("%B " + "%d " + "%Y"),
            "likes": 0,
            "recipe_servings": request.form.get("recipe_servings"),
            "recipe_duration": request.form.get("recipe_duration")
        }
        mongo.db.recipes.insert_one(new_recipe)

        # Taking new user to their Profile page
        return redirect(url_for("profile", username=session["this_user"]))

    return render_template("all_recipes.html")


@app.route("/all_recipes")
def all_recipes():
    all_recipes = mongo.db.recipes.find()

    return render_template("all_recipes.html", recipes=all_recipes)


@app.route("/chosen_recipe/<recipe_id>")
def chosen_recipe(recipe_id):
    if not session.get("this_user"):
        return redirect(url_for("error401"))

    # Get all data for chosen/selected recipe
    this_recipe = mongo.db.recipes.find_one({
        "_id": ObjectId(recipe_id)
    })

    # Turning the recipe ingredients and instructions into a list
    recipe_ingredients = this_recipe["recipe_ingredients"]
    recipe_ingredients_into_list = re.split("\*", recipe_ingredients)
    recipe_instructions = this_recipe["recipe_instructions"]
    recipe_instructions_into_list = re.split("\*", recipe_instructions)

    return render_template("chosen_recipe.html", recipe=this_recipe, ingredients=recipe_ingredients_into_list, instructions=recipe_instructions_into_list)


# ------------------- My recipes page (templates/my_recipes.html)
@app.route("/my_recipes")
def my_recipes():
    all_recipes = mongo.db.recipes.find()

    return render_template("my_recipes.html", recipes=all_recipes)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove(
        {"_id": ObjectId(recipe_id)}
    )
    return redirect(url_for("my_recipes"))


# ------------------- Edit recipe page (templates/edit_recipe.html)
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, {"$set": {
            "recipe_name": request.form.get("recipe_name"), 
            "recipe_description": request.form.get("recipe_description"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_instructions": request.form.get("recipe_instructions"),
            "recipe_servings": request.form.get("recipe_servings"),
            "recipe_duration": request.form.get("recipe_duration")
            }})
        return redirect(url_for("my_recipes"))

    this_recipe = mongo.db.recipes.find_one({
        "_id": ObjectId(recipe_id)
    })

    return render_template("edit_recipe.html", recipe=this_recipe)


# ------------------- Error 401 page (templates/error401.html)
@app.route("/error401")
def error401():
    flash("You do not have access to this page")
    return render_template("error401.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)