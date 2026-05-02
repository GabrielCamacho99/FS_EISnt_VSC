from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from datetime import datetime
import random
import shutil
import os


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
    
@app.route('/api/interactions', methods=['GET'])
def get_interactions():
    try:
        with open('interactions.json', 'r', encoding='utf-8') as f:
            interactions = json.load(f)
        return jsonify(interactions)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    


@app.route('/api/backup', methods=['POST'])
def backup_interactions():
    try:
        # sendBeacon sends as text/plain so we parse it manually
        data = json.loads(request.data)
        username = data.get('name', 'unknown').replace(' ', '_')
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        os.makedirs('backups', exist_ok=True)
        
        # Read current interactions
        with open('interactions.json', 'r', encoding='utf-8') as f:
            interactions = json.load(f)
        
        backup_filename = f'backups/interactions_{username}_{timestamp}.txt'
        
        # Write as readable text instead of JSON
        with open(backup_filename, 'w', encoding='utf-8') as f:
            f.write(f'Backup for user: {username}\n')
            f.write(f'Timestamp: {timestamp}\n')
            f.write('='*40 + '\n\n')
            for entry in interactions:
                f.write(f"User: {entry.get('name', 'N/A')}\n")
                f.write(f"Time: {entry.get('timestamp', 'N/A')}\n")
                f.write(f"Quote: {entry.get('quote', 'N/A')}\n")
                f.write(f"Character: {entry.get('character', 'N/A')}\n")
                f.write(f"Source: {entry.get('source', 'N/A')}\n")
                f.write('-'*40 + '\n')
        
        return jsonify({"status": "backup created", "file": backup_filename}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500








if __name__ == '__main__':
    app.run(debug=True, port=5000)