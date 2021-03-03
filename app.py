# import Flask
from flask import Flask, jsonify

app = Flask(__name__)

# set up routes

# /
@app.route("/")
def welcome():
    "List all all available api routes."
    return (
        f"Available Routes:<br/>"
        f"<a href='/api/v1.0/precipitation'>precipitation</a><br/>"
        f"<a href='/api/v1.0/stations'>stations</a><br/>"
        f"<a href='/api/v1.0/tobs'>tobs</a><br/>"
        f"<a href='/api/v1.0/<start>'>start</a><br/>"
        f"<a href='/api/v1.0/<start>/<end>'>start_end</a><br/>"

    )

# /api/v1.0/precipitation

# /api/v1.0/stations

# /api/v1.0/tobs

# /api/v1.0/<start> and /api/v1.0/<start>/<end>


if __name__ == '__main__':
    app.run(debug=True)