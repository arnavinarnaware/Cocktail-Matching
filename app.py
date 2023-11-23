# app.py
from flask import Flask, render_template, request
from matching import match_cocktail

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', ingredients=["mint", "rum", "sugar", "lime", "soda water", "vodka", "cranberry juice", "orange juice", "vermouth", "lemon"])

@app.route('/match', methods=['POST'])
def match_cocktail_route():
    selected_ingredients = request.form.getlist('ingredients')
    matched_cocktail = match_cocktail(selected_ingredients)
    return render_template('result.html', cocktail=matched_cocktail)

if __name__ == '__main__':
    app.run(debug=True)
