from flask import Flask, render_template
from data import departures, tours

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html", departures=departures, tours=tours)


@app.route("/departures/<departure_id>/")
def departure(departure_id: str):
    return render_template(
        "departure.html", departures=departures, tours=tours, departure_id=departure_id
    )


@app.route("/tours/<int:tour_id>/")
def tour(tour_id):
    return render_template(
        "tour.html", departures=departures, tour_details=tours[int(tour_id)]
    )


if __name__ == '__main__':
    app.run()
