from flask import Flask, jsonify, abort, request
import pandas as pd
from flask_cors import CORS, cross_origin

def load_data():
  csv_data = pd.read_csv("static/input/Data.csv", sep=',')
  csv_data.set_index("countryName")
  return csv_data

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def display_data():
    data = load_data()
    return data[:2].to_json(orient='records')

@app.route('/api/country/getCountries', methods=['GET'])
def get_countrydata():
    data = load_data()
    countryData = data.countryName.unique()
    frameCountry = pd.DataFrame(countryData)
    return frameCountry.to_json(orient='records')

@app.route('/api/type/getDisasterType', methods=['GET'])
def get_disasterType():
    data = load_data()
    disasterTypes = data.disasterType.unique()
    frameType = pd.DataFrame(disasterTypes)
    return frameType.to_json(orient='records')

@app.route('/api/year/getYear', methods=['GET'])
def get_year():
    data = load_data()
    yearRange = data.year.unique()
    yearData = pd.DataFrame(yearRange)
    return yearData.to_json(orient='records')

@app.route('/api/country/getCountries/<string:countryName>', methods=['GET'])
def get_disasterData(countryName):
    data = load_data()
    countryData = data[(data['countryName'] == countryName)]
    return countryData.to_json(orient='records')

@app.route('/api/type/getDisasterType/<string:disasterType>', methods=['GET'])
def get_byType(disasterType):
    data = load_data()
    dataByType = data[(data['disasterType'] == disasterType)]
    return dataByType.to_json(orient='records')

@app.route('/api/yearRange', methods=['GET'])
def get_yearData():
    data = load_data()
    from_year = request.args.get('from')
    to_year = request.args.get('to')
    rangeData = data[(data['year'] == int(from_year)) | (data['year'] == int(to_year))]
    return rangeData.to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True)



  # with open("static/input/Data.csv", "r") as csv_file:
    #     csv_reader = csv.reader(csv_file)
    #     for line in csv_reader:
    #         print(line);
