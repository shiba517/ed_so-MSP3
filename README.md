# MILESTON PROJECT 3 - ēd šo

## OVERVIEW
A study by Colin Camera from Caltech (https://www.caltech.edu/about/news/scientists-uncover-why-you-cant-decide-what-order-lunch-83881) found interesting results for humans with their decision when given a list of options. They found brain activity in the anterior cingulate cortex (ACC) and the striatum to be most active via an fMRI scan in an study where groups of participants were given different number of choices to choose from. From the results, Camera estimated that humans ideal number of choices will range from 8-15 depending on the type of choices.  

Caltech have asked me to create an app/website that will help people make decision on what to cook by giving them a list of recipes.  

## USER EXPERIENCE (UX)
### Project goals
* To make a website where the user will be able to use a CRUD (create, read, update, and delete) function in the form of recipes 
* The website must encourage the user to use the website again via its content (mainly recipes), appearance and ease of navigation


### User stories
* first time visitor goals:
    * As a first time visitor, I want to be able to easily find and see a host of recipes 
    * As a first time visitor, visuals and design of the website must entice me to explore the website 
    * As a first time visitor, I want to see details of the selected recipe in an easy to view layout 
    * As a first time visitor, I should be acknowledged of any dietary elements to the recipe such as meat-free 
* Returning visitor goals 
    * As a returning visitor, I want to be able to know which recipes I have made 
    * Be given suggestions of which recipes to cook 
    * Be able to add to the host of recipes with my own recipes 
    * Able to edit and delete my entries 
    * Search for recipes and even the poster/other users 
* Frequent visitor goals 
    * Save recipes for later viewings 
    * See more and more recipes added to the database 
* Admin goals 
    * Maintain the website 
    * To have the option to delete certain recipes and members 


## THE 5 PLANES
### Strategy 
* Purpose of website? To be a given a database of recipes so they can choose and cook. 
* Target audience? Young adults to mature/elderly adults, and especially those that enjoy cooking 
* Value to the user? Takes away the difficultness of deciding what to eat and makes it a fun way to choose what to eat 
* What will make a good experience? A clean appearance, ability to contribute to an online community, and easy access to sections 
* How are we different? We tell them what they can possibly cook via a short list instead of giving them a database of recipes which they will possibly be overloaded with choices to the point of being put off and cook their usual meal or order a takeaway 
* What we should not do? Simplicity is very much a strong part of the app/website in terms of how we give them a short menu/choices of what to cook; other parts of the website should also follow suite such as the appearance and navigation 

### Scope 
Intended features: 
* A page showing up to 8 recipes for the user to choose from 
* Ability to add, deletes, and edit recipes to add to the host of recipes 
* A profile page showing the users previous made recipes, their contributions and to delete their account 
Content: 
* Simple appearance  
* Engaging writing 
Future features: 
* To be able to leave comments/reviews of the recipes 

### Structure
A non-linear structure/navigation will be used as there will be a few links. The host of recipes will be the main reason as it will not nice for the viewer to see every recipe; with all its details, in a nonlinear structure.

Interaction design:  
* The layout of the website must be consistent for ease of learning and using of the website which includes colour and visual content (e.g. All forms must have curved edges and with a pink background). 
* Error pages should be made which will be much more visually and mentally pleasant than the default browsers default page. Have it lead to a the home page or a relevant page. 

Information architecture:

* [Sitemap](readme_files/images/sitemmap.png)

### Skeleton
Laptop/PC Version
* Black and white
    * Home page - [image](readme_files/images/home_page_top.png) [image](readme_files/images/home_page_bottom.png)
    * Login page - [image](readme_files/images/login_page.png)
    * Register page - [image](readme_files/images/register_page.png)
    * Profile page - [image](readme_files/images/profile.png)
    * All recipes page - [image](readme_files/images/all_recipes.png)
    * Random recipes page - [image](readme_files/images/random_recipes_page.png)
    * My recipes page - [image](readme_files/images/my_recipes.png)
    * Edit recipe page - [image](readme_files/images/edit_recipe_page.png)
    * Add recipe page - [image](readme_files/images/add_recipe_page.png)

Mobile Version
* Black and white
    * Home page - [image](readme_files/images/home_page_mobile_mobile.png) [image](readme_files/images/home_page_bottom_mobile.png)
    * Login page - [image](readme_files/images/login_page_mobile.png)
    * Register page - [image](readme_files/images/register_page_mobile.png)
    * Profile page - [image](readme_files/images/profile_page_mobile.png)
    * All recipes page - [image](readme_files/images/all_recipes_page_mobile.png)
    * Random recipes page - [image](readme_files/images/random_recipes_page_mobile.png)
    * My recipes page - [image](readme_files/images/my_recipes_page_mobile.png)
    * Edit recipe page - [image](readme_files/images/edit_recipe_page_mobile.png)
    * Add recipe page - [image](readme_files/images/add_recipe_page_mobile.png)

### Surface
Colour scheme:
* A shade of dark turqiouse - #026670/rgb()
* A shade of light turqiouse - #9FEDD7/rgb()
* A shade of light cream - #FEF9C7/rgb()
* A shade of pale yellow - #FCE181/rgb()
* A very light shade of cream - #EDEAE5/rgb()

Font:
* Main headings - [link](https://fonts.google.com/specimen/Rubik#standard-styles)
* Regular text - Montserrat 


## FEATURES
### Existing features 
* Header tag of .html files will contain the navbar. This navbar will include the website logo which when clicked, will direct the user to the home page. It will also contain the links to different parts of the website. Which links to appear will depend on whether the user is logged in or not 
* Footer tag of .html files will contain links to the websites social-media pages. Due to the nature of this project, the links will take the user to the social media home page; there will be no social media accounts for this website. 
* Home page (home.html) will consist of the website logo and slogan in the middle of the page. Underneath that will contain buttons leading to the registration page and further down the home page. Underneath this area will be another part of the home page which will contain information on how the website works. 
* Login page (login.html) will contain a form for the user to fill out in order to gain access to parts of the websites that is not the ‘home’, ‘register’ and a limited ‘all recipes’ page. Completing this form will lead the user to their very own ‘profile’ page. 
* Register page (register.html) will contain a form for the user to log back in the website. This will lead the user to the ‘profile’ page. 
* Profile page (profile.html) will contain a welcome message, information regarding the users username, registration date and how many recipes the user has uploaded. From this website, the links to more parts of the website will be accessible.  
* All recipes page (all_recipes.html) will contain all the recipes in the websites database. It will be displayed via an image and its title. Clicking on the title will lead the user another page (chosen_recipe.html) containing more information on the recipe. 
* Chosen recipe page (chosen_recipe.html) will contain a picture of the recipe, the name, description, ingredients, instructions and further details such as name of the user who posted it, timings of making the recipe, how many people it can feed and the amount of likes it has received. 
* Random recipes page (random_recipes.html) will contain three recipes from the database chosen at random 
* Logout link will log the user out 
* Remove link will remove the user from the database and all their recipes that they have posted. It will ask via  a modal whether they are sure they want this to happen. 
* Edit Recipe page (edit_recipe.html) will let the user edit their own recipes. This will button will only appear on the users recipes when on the selected recipes ‘chosen recipe’ page 
* Delete button will let the user delete their chosen recipe. It will ask via a modal whether they are sure they want this to happen. 
