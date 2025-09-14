# /backend/app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    video_url = data.get('url')
    
    # Placeholder response
    return jsonify({"summary": "Video analysis coming soon..."})

if __name__ == '__main__':
    app.run(debug=True)
