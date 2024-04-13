
from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

API_KEY = '3f23026f3d2e4867a4b6f25b864618cc'
BASE_URL = 'https://api.spoonacular.com/recipes'

@app.route('/')
def index():
    return render_template('search.html')
#i hope u can understand this
@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    url = f'{BASE_URL}/complexSearch?query={query}&apiKey={API_KEY}'
    response = requests.get(url).json()
    recipes = response.get('results', [])
    return render_template('results.html', recipes=recipes)

@app.route('/recipe/<int:recipe_id>')
def recipe_details(recipe_id):
    url = f'{BASE_URL}/{recipe_id}/information?apiKey={API_KEY}&includeNutrition=false'
    response = requests.get(url).json()
    if response:
        ingredients = [{'original': ingredient['original']} for ingredient in response.get('extendedIngredients', [])]
        instructions = response.get('instructions', '').split('\n')
        return render_template('recipe.html', recipe=response, ingredients=ingredients, instructions=instructions)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
# API key from Google Developer Console: AIzaSyBQdJLrX59G34jY0mW18-6lK  
