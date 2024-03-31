from flask import Flask, render_template

app = Flask(__name__)

# Sample data (replace with your actual recommendation logic)
user_preferences = {
    "cuisine": "italian",
    "dietary_preferences": ["vegetarian"],
    "spice_level": "mild",
    "food_allergies": "no",
    "mood": "happy"
}

# Sample recommended dishes with images (replace with your actual recommendation logic)
recommended_dishes = [
    {"name": "Pasta Alfredo", "image": "dish1.jpg"},
    {"name": "Margherita Pizza", "image": "dish2.jpg"},
    # Add more dishes...
]

@app.route('/')
def index():
    return render_template('index.html', user_preferences=user_preferences, recommended_dishes=recommended_dishes)

if __name__ == '__main__':
    app.run(debug=True)
