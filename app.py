import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'RecipeBook'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    '''This displays all the recipes on the landing page'''
    recipes_count = mongo.db.Recipes.count()
    return render_template("recipes.html", recipes=mongo.db.Recipes.find(), courses=mongo.db.Course.find(), recipes_count=recipes_count)


@app.route('/sort_az')
def sort_az():
    '''This sorts the recipes alphabetically ascending'''
    recipes_count = mongo.db.Recipes.count()
    recipes = mongo.db.Recipes.find().sort("lowercase_name", 1)
    
    return render_template("recipes.html", recipes=recipes, courses=mongo.db.Course.find(), recipes_count=recipes_count)


@app.route('/sort_likes_ascending')
def sort_likes_ascending():
    '''This sorts the recipes displayed by the ammount of likes each recipe has in ascending order'''
    recipes_count = mongo.db.Recipes.count()
    return render_template("recipes.html", recipes=mongo.db.Recipes.find().sort("likes", 1), courses=mongo.db.Course.find(), recipes_count=recipes_count)

@app.route('/sort_likes_descending')
def sort_likes_descending():
    '''This sorts the recipes displayed by the ammount of likes each recipe has in decending order'''
    recipes_count = mongo.db.Recipes.count()
    return render_template("recipes.html", recipes=mongo.db.Recipes.find().sort("likes", -1), courses=mongo.db.Course.find(), recipes_count=recipes_count)


@app.route('/get_course/<course>')
def get_course(course):
    '''This displays a filtered view of the recipes by the course the user has selected'''
    recipes = mongo.db.Recipes.find({"course_name": course})
    recipes_count = mongo.db.Recipes.count({"course_name": course})

    return render_template("recipes.html", recipes=recipes, courses=mongo.db.Course.find(), recipes_count=recipes_count)    


@app.route('/show_recipe/<recipe_id>')
def show_recipe(recipe_id):
    '''This dispalys the full recipe of which the user has clicked'''
    this_recipe = mongo.db.Recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("fullrecipe.html", recipe=this_recipe, icon="favorite_border")


@app.route('/like/<recipe_id>')
def like(recipe_id):
    '''This increments the likes for the recipe by one each time a user clicks on the like icon'''
    mongo.db.Recipes.update({'_id': ObjectId(recipe_id)},
                            { "$inc": {'likes': 1} })

    this_recipe = mongo.db.Recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("fullrecipe.html", recipe=this_recipe, icon="favorite")    

    
@app.route('/add_recipe')
def add_recipe():
    '''This returns an add recipe form'''
    return render_template("addrecipe.html", courses=mongo.db.Course.find(), cuisines=mongo.db.Cuisine.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    '''This takes the add recipe form data and inserts it in to the Recipe collection as a document in MongoDB
    then redirects back to recipes.html to view the newly added recipe. prep and cook times are added together to return a total cook time.'''
    ingredients = request.form["ingredients"].split("\n")
    method = request.form["method"].split("\n")
    
    int_prep = int(request.form["prep"])
    int_cook = int(request.form["cook"])
    int_total_time = int_prep + int_cook
    total_time = str(int_total_time)

    lowercaseName = request.form["name"].lower()
    
    mongo.db.Recipes.insert_one({'lowercase_name': lowercaseName,
                                'name': request.form["name"],
                                'author': request.form["author"],
                                'cuisine_name': request.form["cuisine_name"],
                                'course_name': request.form["course_name"],
                                'likes': 0,
                                'cals': request.form["cals"],
                                'prep': request.form["prep"],
                                'cook': request.form["cook"],
                                'total_time': total_time,
                                'ingredients': ingredients,
                                'method': method})

    return redirect(url_for('get_recipes'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    '''This returns an add recipe form'''
    this_recipe = mongo.db.Recipes.find_one({"_id": ObjectId(recipe_id)})

    return render_template("editrecipe.html", recipe=this_recipe, courses=mongo.db.Course.find(), cuisines=mongo.db.Cuisine.find())


@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    '''This updates an existing recipe'''
    ingredients = request.form["ingredients"].split("\n")
    method = request.form["method"].split("\n")
        
    int_prep = int(request.form["prep"])
    int_cook = int(request.form["cook"])
    int_total_time = int_prep + int_cook
    total_time = str(int_total_time)
    lowercaseName = request.form["name"].lower()

    mongo.db.Recipes.update({'_id': ObjectId(recipe_id)},
                            {'lowercase_name': lowercaseName,
                            'name': request.form["name"],
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


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    '''This removes a recipe from the database'''
    mongo.db.Recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            )