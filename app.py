from data import tours, departures
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/departures/<departure>/")
def departure(departure):
    return render_template("departure.html")


@app.route("/data/tours/<int:tour_id>") # TODO: delete this route after doing extra-exercises
@app.route("/tours/<int:tour_id>")
def tour(tour_id):
    return render_template("tour.html", tour_details=tours[tour_id], departures=departures)


@app.route("/data/")
def data():
    return render_template("dop.html", tours=tours)


if __name__ == '__main__':
    app.run("localhost", 8000, debug=True)
