from flask import Flask, request, jsonify
from words import words as words_list
from generator import WordSearch
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def generate_word_search(words) -> tuple:
    grid = WordSearch(words)
    return { 'search': grid.generate_word_search(), 'words': grid.words_copy }

@app.route('/generate_word_search', methods=['POST'])
def generate_word_search_route():
    try:
        data = request.get_json()
        words = data.get('words', [])
    except:
        words = [random.choice(words_list) for _ in range(15)]

    if not words:
        words = [random.choice(words_list) for _ in range(15)]
    result = generate_word_search(words)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)