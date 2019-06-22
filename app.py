import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'RecipeBook'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

'''This function displays all the recipes on the landing page'''
@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.Recipes.find())

@app.route('/get_course/<course>')
def get_course(course):
    recipes = mongo.db.Recipes.find({"course_name": course})
    return render_template("recipes.html", recipes=recipes)    

'''This function dispalys the full recipe of which the user has clicked'''
@app.route('/show_recipe/<recipe_id>')
def show_recipe(recipe_id):
    this_recipe = mongo.db.Recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("fullrecipe.html", recipe=this_recipe)
 
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)