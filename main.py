from flask import Flask, render_template, redirect, url_for, request
import requests
from tokens import api_key

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/characters", methods=["GET", "POST"])
def get_characters():
    authorization_header = {
        "Accept": "application/json",
        "Authorization": "Bearer " + api_key
    }
    response = requests.get("https://the-one-api.dev/v2/character", headers=authorization_header)
    response.raise_for_status()

    characters = response.json()

    if request.method == "POST":
        race = request.form.get("race")

        response = requests.get(f"https://the-one-api.dev/v2/character?race={race}", headers=authorization_header)
        response.raise_for_status()

        characters = response.json()

        return render_template("characters.html", characters=characters["docs"])

    else:
        return render_template("characters.html", characters=characters["docs"])
    

@app.route("/movie", methods=["GET", "POST"])
def get_movies():
    authorization_header = {
        "Accept": "application/json",
        "Authorization": "Bearer " + api_key
    }

    response = requests.get("https://the-one-api.dev/v2/movie", headers=authorization_header)
    response.raise_for_status()

    movies = response.json()

    return render_template("movies.html", movies=movies["docs"])

if __name__ == "__main__":
    app.run(debug=True)