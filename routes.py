from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/searchfilms/<name>")
def search_films(name):
    films = [
        "The Shawshank Redemption",
        "The Godfather",
        "The Godfather: Part II",
        "Il buono, il brutto, il cattivo.",
        "Pulp Fiction",
        "Inception",
        "Schindler's List",
        "12 Angry Men",
        "One Flew Over the Cuckoo's Nest",
        "The Dark Knight",
        "Star Wars: Episode V - The Empire Strikes Back",
        "The Lord of the Rings: The Return of the King",
        "Shichinin no samurai",
        "Star Wars",
        "Goodfellas"
    ]

    results = []

    for f in films:
        if f.lower().startswith(name.lower()):
            results.append(f)

    return jsonify(results)


@app.route("/api/getteams")
def get_teams():
    teams = [
        "Tottenham",
        "Chelsea",
        "Arsenal",
        "Manchester United",
        "Manchester City",
        "Liverpool",
        "Everton"
    ]

    return jsonify(teams)

if __name__ == "__main__":
    app.run(debug=True)