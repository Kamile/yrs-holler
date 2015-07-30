from flask import Flask
from flask import request
import pickle

app = Flask("Cats Against Catcalling")
data_file = "holler.dat"

class Catcall:
    """Class to define object containing location and timestamp of the catcall that was recorded"""
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
    
    """#TESTING -- ADDING EMPTY ARRAY DELETE THIS AFTERWARDS

    #---------------------------------------------------------

    with open(data_file, 'wb') as output: #save data
        pickle.dump([], output, pickle.HIGHEST_PROTOCOL)

    #---------------------------------------------------------
    """

    catcallList = []

    with open(data_file, 'rb') as input:
        for item in range(pickle.load(input)):
            catcallList.append(pickle.load(input))
        #catcallList = pickle.load(input)  #retrieve


    #add most recent catcall to file
    catcallList.append(catcall)

    with open(data_file, 'wb') as output: #save data
        pickle.dump(len(catcallList), output)
        for item in catcallList:
            pickle.dump(item, output)
        #pickle.dump(catcallList, output, pickle.HIGHEST_PROTOCOL)

    del catcall

    returnText = ""
    for holler in catcallList:
        returnText = returnText + "\n" + holler.print_data()

    return returnText
    
    #return catcall.print_data();


if __name__ == "__main__":
    app.debug = True
    app.run()


