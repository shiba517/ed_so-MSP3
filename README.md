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
    * As a returning visitor, I want to be given suggestions of which recipes to cook 
    * As a returning visitor, I want to be able to add to the host of recipes with my own recipes 
    * As a returning visitor, I want to be able to edit and delete my entries 
    * As a returning visitor, I want to search for recipes and even the poster/other users 
* Frequent visitor goals 
    * As a frequent visitor, I want to save recipes for later viewings 
    * As a frequent visitor, I want to see more and more recipes added to the database 
* Admin goals 
    * As an admin, I want to maintain the website 
    * As an admin, I want to to have the option to delete certain recipes and members 


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

### Future features 
* A logo that is not a icon from fontawsome.com
* To be able to display recipes in specefic orders such as by name, name of poster etc
* Adding a favourite/save for later section


## TECHNOLOGIES USED
* HTML
* CSS
* Materialize - a .css library which also includes use of .js
* Font awesome - a catalogue of icons for .html files
* Jquery - A convenient JS library
* Github - Save and deploy projects useing this
* Git pod - Platform to write code
* Balsamiq - software for use fo making skeleton sketches
* Lucid chart - website where you can make flowcharts
* W3C Markup Validator - detects any errors in .html files
* W3C CSS Validator - detects any errors in .css files

## TESTING
### User stories testing
AIM | Achieved?
--- | --- |
As a first time visitor, I want to be able to easily find and see a host of recipes | yes
As a first time visitor, visuals and design of the website must entice me to explore the website | yes 
As a first time visitor, I want to see details of the selected recipe in an easy to view layout | yes 
As a first time visitor, I should be acknowledged of any dietary elements to the recipe such as meat-free | not yet 
As a returning visitor, I want to be able to know which recipes I have made  | yes 
As a returning visitor, I want to be given suggestions of which recipes to cook  | yes 
As a returning visitor, I want to be able to add to the host of recipes with my own recipes  | yes 
As a returning visitor, I want to be able to edit and delete my entries  | yes 
As a returning visitor, I want to search for recipes and even the poster/other users  | yes 
As a frequent visitor, I want to save recipes for later viewings  | not yet
As a frequent visitor, I want to see more and more recipes added to the database  | yes 
As an admin, I want to maintain the website  | not yet
As an admin, I want to to have the option to delete certain recipes and members | not yet 

### CRUD (create, read, update, and delete) testing
AIM | Achieved?
--- | --- |
Can a user create a recipe? | yes 
Can a user read(view) a recipe? | yes 
Can a user update a recipe? | yes 
Can a user delete a recipe? | yes 

### Home page testing (home.html)
AIM | Achieved?
--- | --- |
Any user clicking on 'more' button will lead to a smoothe scrolldown to the 'how it works' section of the homepage
Any user can click on the 'register' button
Any user clicking on either 'register' buttons will lead to the register.html
Any user clicking on 'login' button will lead to login.html
'register' button will not appear when a user is logged in

### Navbar testing
AIM | Achieved?
--- | --- |
Clicking on the logo will lead user to the home.html
When user is not logged in, only link that will appear will be 'All recipes', 'Login', and 'Register'
When user is logged in, the links on show will be 'All recipes', 'Random', 'Profile', and 'Logout'
Clicking on 'logout' will lof the user out if his/her account and back to home.html

### Register testing
AIM | Achieved?
--- | --- |
'username' will only take in aplabetical characters(upper and lower case) and numbers
'username' will only take upto 20 characters
'username' will take a minimum of 5 characters
'password' will only take in aplabetical characters(upper and lower case) and numbers
'password' will take a minimum of 5 characters
'password' will only take upto 20 characters
Clicking on 'login from here' will take the user to the login.html
Clicking on 'sign up' will update the intended mongo database (mongo.db.users)
Clicking on 'sing up' will also taek the user to their profile page (profile.html)

### Login testing
AIM | Achieved?
--- | --- |
'username' will only take in aplabetical characters(upper and lower case) and numbers
'username' will only take upto 20 characters
'username' will take a minimum of 5 characters
'password' will only take in aplabetical characters(upper and lower case) and numbers
'password' will take a minimum of 5 characters
'password' will only take upto 20 characters
Clicking on 'register from here' will take the user to the login.html
Clicking on 'login' will also take the user to their profile page (profile.html) if successful
If clicking on 'login' and app.py did not find a match in the details entered, a flash message of "Username and/or password is incorrect" will appear
If clicking on 'login' and app.py did not find a match in the details entered, details entered will be cleared from the form

### Profile testing
AIM | Achieved?
--- | --- |
Username of the user will appear near the top of the page
Buttons of 'Add', 'Mine', 'Random' and 'Bye' will appear on screen
Clicking on 'add' will take user to the add_recipe.html
Clicking on 'mine' will take user to the my_recipes.html
Clicking on 'random' will take user to the random_recipes.html
Clicking on 'bye' will lead to a modal appearing
The modal will ask 'Delete?' with a follow message 'Clicking yes will permanently delete your account and all your recipes'
Clicking on 'no' will remove the modal
Clicking on 'yes' will delete the user from the intended monog database (mongo.db.users)
Clicking on 'yes' will also lead the user back to the home.html
On the right will be a card of the most popular recipe based on the ammount of likes

### All recipes testing
AIM | Achieved?
--- | --- |
A host of cards should appear containing a picture, title, information regarding likes, servings, and cooking duration from the mongo database (mongo.db.recipes)
Quantity of cards on show will match the quantity of entries in the mongo database that it is coming from
Clicking on the 'i' icon should lead to another card sliding up contained the name of the recipe and the description
Clicking on 'lets make this' will lead teh user to chosen_recipe.html
If user is not logged in, 'like' icon will not be functional
If user is not logged in, 'lets make this' link will not be visible

### Chosen recipes
AIM | Achieved?
--- | --- |
Image of recipe should be near the upper left of the scren
Recipe name, username, creation date, likes, servings, cooking curation, and recipe description should appear near the upper right of the screen
Clicking on the 'like' icon (heart) will increment the number below it by 1
Recipe ingredients list should appear near the lower left of the screen
Recipe instructions list should appear near the lower right of the screen
Recipe ingredints will appear in an unordered list format
Recipe instructions will appear in an ordered list format
Bottom corner of the screen should have a 'plus' icon if the recipes was posted by the user logged in
Clicking on the 'plus' icon will lead to the icons of 'delete' and 'edit' to appear
Clicking on the 'edit' icon will lead user to the edit_recipe.html
Clicking on 'delete' icon will lead to a modal appearing
The modal will ask 'Delete?' with a follow message 'Clicking yes will permanently delete this recipe'
Clicking on 'no' will remove the modal
Clicking on 'yes' will delete the recipe from the intended monog database (mongo.db.recipes)
clicking on 'yes' will also lead the user back to the all_recipes.html

### Edit recipe
AIM | Achieved?
--- | --- |
Each field on the form should match the information on the mongo databse of the recipe chosen to edit
Clicking on any field should give the user the ability to change the inputs
Clicking on 'edit' will update the informatino of that recipe in the mongo database
Clicking on 'edit' will also then lead the user to the all_recipes.html
Changed information of edited recipe should be visible in ohter pages the recipe appears in (all_recipes.html, chosen_recipes.html, and my_recipes.html)

### Add recipe testing
AIM | Achieved?
--- | --- |
'recipe name' field should take in any characters
'recipe name' will take upto 100 characters in length
'recipe description' field will take in any characters
'recipe description' field size should accomodate the entered information
'recipe ingredients' field will take in any characters
'recipe ingredients' field size should accomodate the entered information
'recipe instructions' field will take in any characters
'recipe instructions' field size should accomodate the entered information
'recipe image url' field will take in url text
'recipe imahe url' field size should accomodate the entered information
'servings' will only take in numbers
'servings' will take in a number of maximum of 2 digits long
'duration' will only take in numbers
'duration' will take in a number of maximum of 4 digits long
Clicking on 'share' will update the relevant mongo database
Clicking on 'share' will also lead teh user to the all_recipes.html

### My recipes testing
All recipe cards on show will be recipes posted by the user

### Random recipes testing
Three cards will be on show
Recipe cards will change each time random.html is clicked

### Security
When logging out, session cookie of user will be deleted
If session cookie of user is not in storage whilst navigating away from the 'profile' page whilst logged in, page will lead to an error 401 page
If session cookie of user is not in storage whilst navigating away from the 'all recipes' page whilst logged in, page will lead to an error 404 page
If session cookie of user is not in storage whilst navigating away from the 'random recipes' page whilst logged in, page will lead to an error 404 page
If session cookie of user is not in storage whilst navigating away from the 'add recipe' page whilst logged in, page will lead to an error 404 page
If session cookie of user is not in storage whilst submittin a form from the 'add_recipe' page whilst logged in, page will lead to an error 401 page
If session cookie of user is not in storage whilst submittin a form from the 'add_recipe' page whilst logged in, relevant mongo database will not be updated
If session cookie of user is not in storage whilst navigating away from the 'my recipes' page whilst logged in, page will lead to an error 401 page
If session cookie of user is not in storage whilst navigating away from the 'chosen recipe' page whilst logged in, page will lead to an error 401 page
If session cookie of user is not in storage whilst navigating away from the 'edit recipe' page whilst logged in, page will lead to an error 404 page
If session cookie of user is not in storage whilst submittin a form from the 'edit_recipe' page whilst logged in, page will lead to an error 401 page
If session cookie of user is not in storage whilst submittin a form from the 'edit_recipe' page whilst logged in, relevant mongo database will not be updated
If session cookie of user is not in storage whilst clicking on the 'delete' button and then followed by the 'yes' button in the 'profile' page, page will lead to an error 404 page
If session cookie of user is not in storage whilst clicking on 'yes' to delete the account, the relevant mongo database will not be updated


## DEPLOYMENT
### Github pages
The website was deployed onto GitHub via the following steps: 
1. Logging into my GitHub account and creating a new repository
2. Under the subheading ‘Repository template’, I chose the template given to me by Code Institute from the drop-down menu
3. I named my repository under the subheading ‘Repository name’ and then clicked on the green button named ‘Create repository’.
4. Once the repository was created, I was lead to my repository page. From here, I clicked on the ‘Settings’ button near the top of the page
5. Scroll down to the ‘GitHub Pages’ section and click on the text, ‘Check it out here!’, which will be in blue
6. Under the subheading ‘Source’, click on its only drop-down menu and select ‘Master’ and then click on the button ‘Save’
7. The repository webpage will now have been created and the link will now be shown to you for your use

### Making A Local Clone
You may want to have access via a copy of the repository on your own device. There are three ways to do this: 
* Method 1
1. Login to your GitHub account and open up the repository you would like to copy 
2. Click on the button with a drop-down menu named ‘Code’ which will be placed next to the green ‘Gitpod’ button
3. You will then have the option to download it on to your system via the ‘Download ZIP’ option

* Method 2 
1. Open up your preferred IDE and open up the folder where you would the repository to be copied/cloned
2. In the terminal, type in ‘git clone’ ; do not press enter or anything else
3. Now login to your GitHub account and open up the repository you would like to copy
4. Click on the ‘Code’ button again and copy the text given under the subheading ‘HTTPS’. A button next to this text gives you an easier way of copying the text
5. Back to your IDE terminal, after the ‘git clone’, press the spacebar button and paste in the link you copied from the repository. Your entry in the terminal should look something like this: ‘gti clone https://github.com/shiba517/MSP2-The-Memory-Game.git’. Then press enter
6. Your terminal will let you know the repository has been cloned and saved to your preferred destination and will be evident when viewing files and folders from your preferred destination

## CREDITS
### Content
* Inpsiration for the fictional story of the aim of the making of the website, written in the Overview section, was inspired by an article found on caltech.edu - [link](https://www.caltech.edu/about/news/scientists-uncover-why-you-cant-decide-what-order-lunch-83881)
* All written content on the website was created by me

### Media
* Colour scheme (#50) by **Five Hundred** - https://visme.co/blog/website-color-schemes/
* Typography for headings by **Johan Aukerlund** - https://fonts.google.com/specimen/Rubik#standard-styles 
* Typography for non-headings by **Julieta Ulanovsky, Sol Matas, Juan Pablo del Peral, Jacques Le Bailly** - https://fonts.google.com/specimen/Montserrat?query=montserrat
* Illustration by **Freepic.com** via **Flaticon** - https://www.flaticon.com/authors/kawaii/lineal-color
