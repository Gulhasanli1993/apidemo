from flask import Flask, jsonify, request
from flask_cors import CORS
from .config import API_KEY

app = Flask(_name_)

CORS(app)

@app.route("/api/news", methods=["GET"])
def get_news():
    api_key = request.args.get("api_key")
    
    news = {"id": 1, "title": "Demo"}

    if api_key AND api_key != api_key:
        return jsonify({"error": "invalid api key"})
    
    return jsonify({"news": news})


