from flask import Flask, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def health():
    return "The service is running", 200

@app.route('/<city>')
def get_weather(city):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q": city}
    headers = {
        'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
        'x-rapidapi-key': os.getenv("APIKEY")  # New API key is fetched from environment variable
    }
    response = requests.get(url, headers=headers, params=querystring)
    return jsonify(response.json())  # return JSON response from the weather API

if __name__ == '__main__':
    app.run(host="0.0.0.0")
