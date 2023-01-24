from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.recipe import Recipe

# ! READ
@app.route('/recipes')
def dashboard():
    if 'user_id' not in session:
        redirect('/users/logout')
    return render_template('home.html', recipes = Recipe.get_all_user_recipes())

@app.route('/recipes/<int:id>')
def show_recipe(id):
    return render_template('recipe.html', recipe = Recipe.get_one({'id' : id}))

# ! CREATE
@app.route('/recipes/new')
def new_recipe():
    if 'user_id' not in session:
        redirect('/users/logout')
    return render_template('new.html')

@app.route('/recipes/create', methods=['POST'])
def save_recipe():
    print(request.form)
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    return redirect('/recipes/' + str(Recipe.save(request.form)))

# ! UPDATE
@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        redirect('/users/logout')
    return render_template('edit.html', recipe = Recipe.get_one({'id' : id}))

@app.route('/recipes/update', methods=['POST'])
def update_recipe():
    print(request.form)
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/edit/' + request.form['id'])
    Recipe.update_recipe(request.form)
    return redirect('/recipes')

# ! DELETE
@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
    Recipe.delete_recipe({'id' : id})
    return redirect('/recipes')