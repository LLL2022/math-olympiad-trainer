import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample database of random text
text_database = [
    "The quick brown fox jumps over the lazy dog.",
    "Curiosity killed the cat, but satisfaction brought it back.",
    "The only way to do great work is to love what you do.",
    "You miss 100% of the shots you don't take.",
    "Simplicity is the ultimate sophistication."
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_random_text', methods=['GET'])
def get_random_text():
    # Get a random text from the database
    random_text = random.choice(text_database)
    return jsonify(random_text)

if __name__ == '__main__':
    app.run(debug=True)