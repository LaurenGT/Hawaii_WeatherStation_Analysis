# import dependencies
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database setup
engine = create_engine(f"sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

# Flas setup
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