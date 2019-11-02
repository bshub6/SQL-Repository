#Dependencies
from flask import Flask, jsonify
import numpy as np
import pandas as pd
import dateline as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model

Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

#variables for bases
measurement = Base.classes.measurement
station = Bases.classes.station

session = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    print ("Server received request for 'Home' page")
    return "Welcome to the Surf's Up Weather API"


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to the Hawaii recipitation and Temperature Information API.<br/>"
        f"Available Routes:<br/>"
        f"Here are the available API Calls:<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start date<br/>"
        
    )
#precipation API call
@app.route("/api/v1.0/precipitation")
def precipitation():
    
    #Create a session to link Python to the DB
    session = Session(engine)
    last12 = dt.date(2015, 7, 17) - dt.timedelta(days=365)
    precip_query = session.query(measurement.date, measurement.prcp).filter(measurement.date>=last12).all()
    precip =  {dt.date(prcp for date, prcp in precip_query)}
    
    session.close()
    
    return jsonify(precip)
           
#station API call

@app.route("/api/v1.0/stations")
def stations():
    station_query = session.query(station.station, station.name).all()
    station - list(np.ravel(station_query))
    
    session.close()
    
    return jsonify(station)

#temp API call
app.route("/api/v1.0/tobs")
def Temperature():
    last12 = dt.date(2017, 7, 1) - dt.timedelta(days365)
    temp = session.query(measurement.date, measurement.tobs).filter(measurement.date >= last12).all()
    tobs = list(np.ravel(temp))
    
    session.close()
    
    return jsonify(tobs)






if __name__ == '__main__':
    app.run(debug=True)
