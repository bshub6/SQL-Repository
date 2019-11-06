#Dependencies



import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


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
station = Base.classes.station



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
        f"/api/v1.0/start/<start><br/>"
        f"/api/v1.0/start/end/<start>/<end>"
        
        
         )
 #station API call

@app.route("/api/v1.0/stations")
def stations():
    #Create a session to link Python to the DB
    session = Session(engine)
    
    station_query = session.query(station.station, station.name).all()
    station - list(np.ravel(station_query))
    
    session.close()
    
    return jsonify(station)
   
    
    
#precipation API call
@app.route("/api/v1.0/precipitation")
def precipitation():
    
    #Create a session to link Python to the DB
    session = Session(engine)
    
    last12 = dt.date(2017, 8, 23) - dt.timedelta(days=366)
    precip_query = session.query(measurement.date, measurement.prcp).filter(measurement.date>=last12).all()
    precip =  {dt.date(prcp for date, prcp in precip_query)}
    
    session.close()
    
    return jsonify(precip)
           
#station API call

#temp API call

app.route("/api/v1.0/tobs")

def Temperature():

    #Create a session to link Python to the DB

    session = Session(engine)

    last12 = dt.date(2017, 8, 23) - dt.timedelta(days=366)
    temp = session.query(measurement.date, measurement.tobs).filter(measurement.date >= last12).all()
    tobs = list(np.ravel(temp))

    
    session.close()

    return jsonify(tobs)

#start date API call
app.route("/api/v1.0/start")
def temp_start():
    #Create a session to link Python to the DB
    session = Session(engine)
    
    start_query = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).filter(measurement.date >= start).all()
    temp = list(np.ravel(start_query))
    
    session.close()
    
    return jsonify(temp)


#date range API Call
app.route("/api/v1.0/start/end")
def temp_date_range(start, end):
    #Create a session to link Python to the DB
    session = Session(engine)
    
    start_end_query = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).filter(measurement.date >= start).filter(measurement.date <= end).all()
    tobs = list(np.ravel(start_end_query))
    
    session.close()
    
    return jsonify(temp)

if __name__ == '__main__':
    app.run(debug=True)
    
    
