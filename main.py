from flask import Flask, jsonify
import os
from doc_plus_pertinent import doc_plus_pertinent

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/api/v1/articles/<string:sujet_rechercher>', methods=['GET'])
def process_json(sujet_rechercher):
    response = doc_plus_pertinent(sujet_rechercher)
    return response


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
