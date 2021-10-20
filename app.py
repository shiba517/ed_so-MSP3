import os
import datetime
import re
import random
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
    # For use when user registers and then persses teh back button on the window
    if session.get("this_user"):
        return redirect(url_for("error404"))

    # When user clicks 'register'
    if request.method == "POST":
        # Checking if username exists
        check_user_exists = mongo.db.users.find_one({
            "username": request.form.get("username").lower()
        })

        # If username has been taken
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
        flash("You are one of us now")

        # Taking new user to their Profile page
        return redirect(url_for("profile", username=session["this_user"]))

    return render_template("register.html")


@app.route("/ban", methods=["GET", "POST"])
def ban():
    if request.method == "POST":
        check_user_exists = mongo.db.users.find_one({
            "username": request.form.get("username").lower()
        })
        mongo.db.recipes.remove(
            {"created_by": check_user_exists["username"]}
        )
        mongo.db.users.remove(
            {"_id": ObjectId(check_user_exists["_id"])}
        )

        flash("that chef has been fired")
        return redirect(url_for("all_recipes"))

    return render_template("ban.html")


# ------------------- Login page (templates/login.html)
@app.route("/login", methods=["GET", "POST"])
def login():
    # For use when user logs in and then persses teh back button on the window
    if session.get("this_user"):
        return redirect(url_for("error404"))

    # When user clicks on 'login' button
    if request.method == "POST":
        # Checks if username is in the database
        check_user_exists = mongo.db.users.find_one({
            "username": request.form.get("username").lower()
        })

        # If username is in teh database
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
    # For security reasons
    if not session.get("this_user"):
        return redirect(url_for("error401"))

    # Detting the document of the user
    user_info = mongo.db.users.find_one({
        "username": username
    })

    # Details of the card that will bo on show
    hot = list(mongo.db.recipes.find().sort("likes", -1).limit(1))

    if session["this_user"]:
        return render_template("profile.html", user=user_info, hott=hot)


# ------------------- Logging out
@app.route("/logout")
def logout():
    session.pop("this_user")
    flash("You have logged out")
    return redirect(url_for("home"))


# ------------------- Add recipe page (templates/add_recipe.html)
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    # For security reasons
    if not session.get("this_user"):
        return redirect(url_for("error401"))

    # When user clicks on 'share'
    if request.method == "POST":
        if not session.get("this_user"):
            return redirect(url_for("error404"))

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
            "recipe_duration": request.form.get("recipe_duration"),
            "recipe_image_url": request.form.get("recipe_image_url")
        }
        mongo.db.recipes.insert_one(new_recipe)
        flash("You have added a recipe")

        # Taking new user to their Profile page
        return redirect(url_for("profile", username=session["this_user"]))

    return render_template("add_recipe.html")


# ------------------- All recipes page (templates/all_recipes.html)
@app.route("/all_recipes")
def all_recipes():
    all_recipes = mongo.db.recipes.find()

    return render_template("all_recipes.html", recipes=all_recipes)


# ------------------- Chosen recipe page (templates/chosen_recipe.html)
@app.route("/chosen_recipe/<recipe_id>")
def chosen_recipe(recipe_id):
    # For security reasons
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
    # For security reasons
    if not session.get("this_user"):
        return redirect(url_for("error401"))

    # Getting the documents for all the recipes; will tehn be filtered in the my_recipes.html
    all_recipes = mongo.db.recipes.find()

    return render_template("my_recipes.html", recipes=all_recipes)


# ------------------- Delete recipe (templates/chosen_recipe.html)
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    # For security reasons
    if not session.get("this_user"):
        return redirect(url_for("error401"))

    # Chosen recipe will now be removed from the database
    mongo.db.recipes.remove(
        {"_id": ObjectId(recipe_id)}
    )

    flash("Recipe deleted")
    return redirect(url_for("my_recipes"))


# ------------------- Edit recipe page (templates/edit_recipe.html)
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    # For security reasons
    if not session.get("this_user"):
        return redirect(url_for("error401"))

    # When user clicks on 'edit' button
    if request.method == "POST":
        # For security reasons
        if not session.get("this_user"):
            return redirect(url_for("error404"))

        # Will now update
        mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, {"$set": {
            "recipe_name": request.form.get("recipe_name"), 
            "recipe_description": request.form.get("recipe_description"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_instructions": request.form.get("recipe_instructions"),
            "recipe_servings": request.form.get("recipe_servings"),
            "recipe_duration": request.form.get("recipe_duration"),
            "recipe_image_url": request.form.get("recipe_image_url")
            }})
        
        flash("Recipe edited")
        return redirect(url_for("my_recipes"))

    # Fields will be prefilled with information from here
    this_recipe = mongo.db.recipes.find_one({
        "_id": ObjectId(recipe_id)
    })

    return render_template("edit_recipe.html", recipe=this_recipe)


# ------------------- Like (templates/all_recipes.html, my_recipes.html, and random_recipes.html)
@app.route("/like/<recipe_id>")
def like(recipe_id):
    # Clicking on the heart icon will increment the likes
    mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, {"$inc": {
        "likes": 1
    }})
    return redirect(url_for("chosen_recipe", recipe_id=recipe_id))


@app.route("/random_recipes")
def random_recipes():
    # For security reasons  
    if not session.get("this_user"):
        return redirect(url_for("error404"))

    all_recipes = list(mongo.db.recipes.find())

    # Process of creating a random selected recipes
    all_recipes_copy = all_recipes
    random_recipes = []
    max_cards = 3
    current_card = 0
    current_user = session["this_user"]

    # If not enough recipes are in the database to create a random selection
    if len(all_recipes) < max_cards:
        while current_card < len(all_recipes):
            random_number = random.randrange(0, len(all_recipes_copy))
            random_recipes.append(all_recipes_copy[random_number])
            all_recipes_copy.pop(random_number)
            current_card += 1
    # If enough recipes are in teh databse to create a random selection
    else:
        while current_card < max_cards:
            random_number = random.randrange(0, len(all_recipes_copy))
            random_recipes.append(all_recipes_copy[random_number])
            all_recipes_copy.pop(random_number)
            current_card += 1

    return render_template("random_recipes.html", recipes=random_recipes)


# ------------------- Search (templates/all_recipe.html, my_recipes.html)
@app.route("/search", methods=["GET", "POST"])
def search():
    # Finding the wanted recipes
    find_this = request.form.get("query")
    all_recipes = list(mongo.db.recipes.find({"$text": {"$search": find_this}}))

    if not session.get("this_user"):
        return redirect(url_for("error404"))

    return render_template("all_recipes.html", recipes=all_recipes)


# ------------------- Remove account (templates/profile.html)
@app.route("/remove_account/<user_id>")
def remove_account(user_id):
    # For security reasons
    if not session.get("this_user"):
        return redirect(url_for("error404"))

    # Removing all recipes owned by that user
    mongo.db.recipes.remove(
        {"created_by": session["this_user"]}
    )

    # And then removing their account form the database
    mongo.db.users.remove(
        {"_id": ObjectId(user_id)}
    )
    session.pop("this_user")

    flash("You are no longer one of us")

    return redirect(url_for('home'))


# ------------------- Error 401 page (templates/error401.html)
@app.route("/error401")
def error401():
    flash("You do not have access to this page")
    return render_template("error401.html")


# ------------------- Error 404 page (templates/error401.html)
@app.route("/error404")
def error404():
    flash("Page not found")
    return render_template("error404.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)