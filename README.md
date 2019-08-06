# Data Centric Milestone Project - Recipe Book

Welcome to my data centric milestone project, for this project I created an online cookbook, that allows users to easily view, create, update and delete recipes.

---

## UX

This web application will be for users who want to store their own recipes and view other users recipes.

### User Stories

- As a user, I want to find recipes, so I can get some ideas of what I want to cook.
- As a user, I want to find recipes based on an spanish cuisine, so I can cook a spanish meal tonight.
- As a user, I want to find breakfast recipes, so I can get some ideas of what I can make for breakfast.
- As a user, I want to view recipes sorted by likes descending, so I can view the most liked recipes in the database easily.
- As a user, I would like to add my own recipe to the database through an easy to use UI, so other users can see my recipe.
- As a user, I would like the ability to update my recipe, so i can correct any mistakes or add a new idea to the recipe.
- As a user, I would like the ability to delete my recipe, so I can remove the recipe from the database when I wish.  

### Wireframes

- [Desktop/Mobile Wireframes **All Recipes Page**](wireframes\recipes.html.jpg)
- [Desktop/Mobile Wireframes **Full Recipe Page**](wireframes\fullrecipe.html.jpg)
- [Desktop/Mobile Wireframes **Add and Edit Recipes Page**](wireframes\addeditrecipe.html.jpg)

---

## Features

### Existing Features

- All recipes page - This is the landing page, on this page users are welcomed with and introduction to the website and all the recipes displayed.
 
- Sort by menu - This is a dropdown menu where users can choose how they would like all of the recipes to be sorted. Users can sort the recipes by either A-Z, likes ascending or likes descending.
  
- Filter by course buttons - Users can click a course button whether it is breakfast, lunch, dinner, desert or beverage and filter down the recipes to display only the recipes that are of that course.

- Recipe cards - Recipe cards are displayed containing basic information about the recipe including the name, course, total likes, calories and total cooking time. These recipe cards are clickable and take users to a full recipe page.

- Add recipe button - This button will take users to an add recipe form where they can fill in the form to create there own recipe and add it to the database.

- Full recipe page - This page displays full recipe to the user which is the recipes name, total likes, authors name, cuisine, course, prep time, cook time, total time, calories, ingredients and method. This page also includes edit and delete buttons.

- Edit recipe page - This page is accessed though the edit recipe button. This page contains an edit recipe form where the form fields are pre filled with the existing data of the recipe so it is easy to edit.

- Delete recipe button - When a user clicks this button the recipe will be removed from the database.

### Features Left to Implement

- User Authentication - Users can create an account for authentiction so they can only edit and remove their own recipes. 
- Recipe Images - Users can upload images of their recipes to the database these will be dispalyed in the recipe cards and in the full recipe page. 

---

## Technologies Used

- **[HTML](https://en.wikipedia.org/wiki/HTML)**
    - This project uses **HTML** to build the foundation of the website and including links to CSS and JavaScript scripts.

- **[CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)**
    - This project uses **CSS** to style the whole website.

- **[Materialize 0.100.2](http://archives.materializecss.com/0.100.2/)**
    - This project uses the **Materialize** library's navigation bar, modal, dropdown menus, buttons, grid system and css helpers.     

- **[JavaScript](https://www.javascript.com/)/[JQuery js](https://jquery.com/)**
    - This project uses **JavaScript**/**JQuery** to initialize the Materialize dropdown menus, navigation bar and modal.

- **[Python](https://www.python.org/)**
    - This project uses **Python** as the back-end programming language.

- **[Flask](https://flask.palletsprojects.com/en/1.0.x/)**
    - This project uses the microframework **Flask** for routes and templating.

- **[MongoDB Atlas/PyMongo](https://www.mongodb.com/)**
    - This project uses **MongoDB Atlas** to store my database and **PyMongo** which is the Python API for MongoDB to connect to and manipulate the data.

- **[Heroku](https://www.heroku.com/)**
    - This project uses the cloud application platform **Heroku** to host the application.

---

## Testing

User scenarios:

1. View Full Recipe:
    1. Initially when you open the applictaion you on the landing page where you can see a preview of all the recipes in the database dispalyed on cards.
    2. Click on one of the cards.
    3. You will be taken to fullrecipe.html. Verify that the full recipe is displayed.

2. Add Recipe:
    1. Go to the navigation menu and click on 'Add recipe' or click on the 'Add your own' button at the bottom of the landing page.
    2. You will be taken to a form on addrecipe.html, fill in all the fields in the form and click on the 'Save' button.
    3. After you have clicked on save you will be redirected back to the landing page and verify that your new recipe is displayed on that page.

3. Edit Recipe:
    1. Click on an existing recipe and you will be taken to fullrecipe.html where you can see the full recipe details.
    2. At the bottom of the page click on the 'Edit' button.
    3. You will be taken to a pre filled form on editrecipe.html, change something in the form and click on the 'Update' button.
    4. After you have clicked on update you will be redirected back to the landing page, find the recipe you updated and verify that your changes have been made on the recipe you updated.

4. Delete Recipe:
    1. Click on an existing recipe and you will be taken to fullrecipe.html where you can see the full recipe details.
    2. At the bottom of the page click on the 'Delete' button.
    3. Verify the delete by clicking on 'Yes, I'm sure' in the warning modal that will popup.
    4. You will be redirected back to the landing page. Verify that the recipe you deleted has been removed from page.         

#### Responsiveness
- I have tested the website extensively on all screen sizes in vertical and portrait mode:
    - Extra small (I phone 5).
    - Small (Samsung Galaxy S8).
    - Medium (I pad, I pad pro).
    - Large (Laptop, Desktop).
    - Extra large (TV).
    - Google Chrome's developer tools to see how the website functioned and looked across all the different device screen sizes.

#### Browser Support
- I tested the website on Chrome, Microsoft Edge and Firefox.

#### Validation
- I have validated the HTML using **[W3C Markup Validation Service](https://validator.w3.org/)**. Unfortunately the W3C HTML Validator shows alot of errors when reading the Jinja templating syntax. But the rest of the HTML is valid.
- I have validated the CSS using **[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)**.

---

## Deployment

### Local Deployment

To run this project locally you will need the following to be installed:

- Python3 to run the application.
- PIP to install all app requirements.
- Any IDE. I used Microsoft Visual Studio Code.
- GIT for version control.

Here are the steps for local deployment:

- Clone or download this repository by clicking the green 'Clone or download' button and unzipping the file that is downloaded, or you can enter the following into your Git CLI terminal:
    - `git clone https://github.com/dan360z/Data-Centric-Project.git` 

- Navigate to the directory where you unpacked the files if you are not already there. 

- Install all requirements from the requirements.txt file using this command:
    - `sudo pip3 -r requirements.txt`

- Create an environment variable on your machine or in a `.env` file for 'MONGO_URI', remember to reference the `.env` file in a `.gitignore` file. The key and value pair will be:
    - MONGO_URI : `'connection string' (This connection string will be given to you by mongoDB when you have created a cluster by clicking on the connect button.)`.

- Sign up for an account on [MongoDB](https://www.mongodb.com) and create a Cluster, inside that Cluster create a Database called RecipeBook. The Collections in that Recipe should be as follows:

#### Course
```
_id: <ObjectId>
course_name: <string>
```
#### Cusisine
```
_id: <ObjectId>
cuisine_name: <string>
```
#### Recipes
```
_id: <ObjectId>
lowercase_name: <string>
name: <string>
author: <string>
cuisine_name: <string>
course_name: <string>
likes: <int>
cals: <string>
prep: <string>
cook: <string>
total_time: <string>
ingredients: <array>
method: <array>
```

- Now you can run your application using the following command in your CLI:
    - `python -m flask run`
- The app should now be running on *local host* `http://127.0.0.1:5000/`. Copy and paste this into a browser of your choice.     

### Remote Deployment

I have deployed this project to [Heroku](https://www.heroku.com/) using the **master** branch on GitHub. To deploy this project on Heroku I took the following steps:

- Sign up for an Heroku account and create a new app.

- Click the Deploy tab, click on Connect GitHub, and Enable Automatic Deployment. When you push your code to GitHub Heroku will automatically deploy your project. 

- In the Heroku Settings tab, click on the Reveal Config Vars button to configure environmental variables as follows:
    - IP : `0.0.0.0`
    - PORT : `5000`
    - MONGO_URI : `'Mongo DB connection string'`

- Create a requirements.txt file so Heroku can install the required dependencies to run the app.
    - `sudo pip3 freeze --local > requirements.txt`

- Create a Procfile to tell Heroku what type of application is being deployed, and how to run it.
    - `echo web: python app.py > Procfile`

- Commit and Push your code to GitHub.

- Go back to Heroku and your application should be successfully deployed. If it is not check the logs they are very informative.

---

## Credits

The background image in this site was obtained from a google images search. Here is the address to the website where the image is from https://www.sanpellegrino.com/media//international/spyc2019/Sanpellegrino_SPYC_teaser_POST_01.jpg.

### Acknowledgements

- [Stack OverFlow](https://stackoverflow.com/). Help with various code related problems.

### Designer/Developer
Recipe Book was designed and developed by **Daniel Field**.