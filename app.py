# import dependencies
import numpy as np
import datetime as dt

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
@app.route("/api/v1.0/precipitation")
def precipitation():
    session=Session(engine)

    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > query_date).order_by(Measurement.date).all()

    session.close()

    all_results=[]
    for result in results:
        result_dict = {}
        result_dict["date"] = result[0]
        result_dict["prcp"] = result[1]
        all_results.append(result_dict)

    #print(twelve_months)
    return jsonify(all_results)

# /api/v1.0/stations
@app.route("/api/v1.0/stations")
def stations():
    session=Session(engine)

    stations = session.query(Measurement.station.distinct()).all()

    session.close()

    #print(twelve_months)
    results = list(np.ravel(stations))
    return jsonify(results)

# /api/v1.0/tobs
@app.route("/api/v1.0/tobs")
def tobs():
    session=Session(engine)

    most_active = "USC00519281"
    most_act_query_date = dt.date(2017, 8, 18) - dt.timedelta(days=365)
    most_act_twelve_months = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date > most_act_query_date).filter(Measurement.station == most_active).order_by(Measurement.date).all()

    session.close()
    all_tobs = []
    for result in most_act_twelve_months:
        all_tobs.append(result[1])

    print(most_act_twelve_months)
    #results = list(np.ravel(most_act_twelve_months))
    return jsonify(all_tobs)

# /api/v1.0/<start> and /api/v1.0/<start>/<end>


if __name__ == '__main__':
    app.run(debug=True)