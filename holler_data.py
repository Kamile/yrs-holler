from flask import Flask
from flask import request
import pickle

app = Flask("Cats Against Catcalling")

class Catcall:
    """Class to define objecy containing location and timestamp of the catcall that was recorded"""
    def __init__(self, latitude, longitude, date, time):
        self.latitude = latitude
        self.longitude = longitude
        self.date = date
        self.time = time
        
        
    
    #add recorded data
    def add_latitude(self, latitude):
        self.latitude = latitude
    
    def add_longitude(self, longitude):
        self.longitude = longitude
    
    def add_date(self, date):
        self.date = date
        
    def add_time(self, time):
        self.time = time

    def print_data(self):
        return self.latitude + "\n" + self.longitude + "\n" + self.date + "\n" + self.time
        



@app.route('/')
def index():
    return 'INDEX PAGE'

@app.route("/add", methods=['GET'])
def save_data():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    date = request.args.get('date')
    time = request.args.get('time')

    catcall = Catcall(latitude, longitude, date, time)

    with open('holler_data.pk1', 'wb') as output: #save data
        pickle.dump(catcall, output, pickle.HIGHEST_PROTOCOL)

    del catcall

    with open('holler_data.pk1', 'rb') as input:
        catcall = pickle.load(input)
        return catcall.latitude #retrieve and print data
    
    #return catcall.print_data();


if __name__ == "__main__":
    app.debug = True
    app.run()


