from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from datetime import datetime
import random

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"})

@app.route('/api/quotes', methods=['GET'])
def get_quotes():
    try:
        with open('quotes.json', 'r', encoding='utf-8') as f:
            quotes = json.load(f)
        random_quote = random.choice(quotes)
        return jsonify(random_quote)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
@app.route('/api/interaction', methods=['POST'])
def log_interaction():
    try:
        # Get data sent from JavaScript
        data = request.get_json()
        
        # Add timestamp
        data['timestamp'] = datetime.now().isoformat()
        
        # Read existing interactions
        with open('interactions.json', 'r', encoding='utf-8') as f:
            interactions = json.load(f)
        
        # Add new interaction to the list
        interactions.append(data)
        
        # Save updated list back to file
        with open('interactions.json', 'w', encoding='utf-8') as f:
            json.dump(interactions, f, indent=2, ensure_ascii=False)
        
        return jsonify({"status": "logged", "interaction": data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500








if __name__ == '__main__':
    app.run(debug=True, port=5000)