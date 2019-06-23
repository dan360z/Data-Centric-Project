import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'RecipeBook'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

'''This displays all the recipes on the landing page'''
@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.Recipes.find())

'''This displays a filtered view of the recipes by the course the user has selected'''
@app.route('/get_course/<course>')
def get_course(course):
    recipes = mongo.db.Recipes.find({"course_name": course})
    return render_template("recipes.html", recipes=recipes)    

'''This dispalys the full recipe of which the user has clicked'''
@app.route('/show_recipe/<recipe_id>')
def show_recipe(recipe_id):
    this_recipe = mongo.db.Recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("fullrecipe.html", recipe=this_recipe)

'''This returns an add recipe form'''    
@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", courses=mongo.db.Course.find(), cuisines=mongo.db.Cuisine.find())

'''This takes the add recipe form data and inserts it in to the Recipe collection as a document in MongoDB
then redirects back to recipes.html to view the newly added recipe. prep and cook times are added together to return a total cook time.'''
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    
    ingredients = request.form["ingredients"].split(".")
    method = request.form["method"].split(".")
    
    int_prep = int(request.form["prep"])
    int_cook = int(request.form["cook"])
    int_total_time = int_prep + int_cook
    total_time = str(int_total_time)
    
    mongo.db.Recipes.insert_one({'name': request.form["name"],
                                'author': request.form["author"],
                                'cuisine_name': request.form["cuisine_name"],
                                'course_name': request.form["course_name"],
                                'cals': request.form["cals"],
                                'prep': request.form["prep"],
                                'cook': request.form["cook"],
                                'total_time': total_time,
                                'ingredients': ingredients,
                                'method': method})

    return redirect(url_for('get_recipes'))

'''This returns an add recipe form'''
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    this_recipe = mongo.db.Recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("editrecipe.html", recipe=this_recipe, courses=mongo.db.Course.find(), cuisines=mongo.db.Cuisine.find())

'''This updates an existing recipe'''
@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):

    ingredients = request.form["ingredients"].split(".")
    method = request.form["method"].split(".")

    int_prep = int(request.form["prep"])
    int_cook = int(request.form["cook"])
    int_total_time = int_prep + int_cook
    total_time = str(int_total_time)

    mongo.db.Recipes.update({'_id': ObjectId(recipe_id)},
                            {'name': request.form["name"],
                            'author': request.form["author"],
                            'cuisine_name': request.form["cuisine_name"],
                            'course_name': request.form["course_name"],
                            'cals': request.form["cals"],
                            'prep': request.form["prep"],
                            'cook': request.form["cook"],
                            'total_time': total_time,
                            'ingredients': ingredients,
                            'method': method})

    this_recipe = mongo.db.Recipes.find_one({"_id": ObjectId(recipe_id)})                         
    return render_template("fullrecipe.html", recipe=this_recipe)
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)