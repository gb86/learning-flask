from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


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