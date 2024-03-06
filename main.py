from flask import Flask, render_template, redirect, url_for
import requests
from tokens import api_key

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/characters")
def get_characters():
    authorization_header = {
        "Accept": "application/json",
        "Authorization": "Bearer " + api_key
    }
    response = requests.get("https://the-one-api.dev/v2/character", headers=authorization_header)
    response.raise_for_status()

    characters = response.json()

    return render_template("characters.html", characters=characters["docs"])

if __name__ == "__main__":
    app.run(debug=True)