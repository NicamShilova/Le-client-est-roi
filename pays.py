# Importing
import json
import csv
import random
import logging

from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
from app import app
from datetime import date



app = Flask(__name__)

# Loading Mongodb
client = MongoClient("mongodb+srv://NicolasCampion:[mot_de_passe]@cluster0.j0t44.mongodb.net/pays?retryWrites=true&w=majority")
db = client.pays


density_category = {"Small":[],"Medium":[],"High":[],"Very high":[]}
data = []

# Issue the serverStatus command and print the results
serverStatusResult = db.command("serverStatus")

# Import csv file to mongodb
with open('countries_cleaned.csv',) as csvfile:
    reader = csv.DictReader(csvfile)
    for rows in reader:
        data.append(rows)
        
doc = db.liste.insert_many(data)

# Display data about country with a keyword
@app.route('/api/countryselection/<country>', methods =["GET"]) 
def info_country(country):

    for land in db.liste.find({"name_country": country},{ "_id": 0, }):
        countryContent = land  

    return jsonify(countryContent)

# Add a new country with random datas
@app.route('/api/addcountry/<country>', methods=['GET'])
def add_country(country):
    
    mydict = {  "name_country": country,
                "population": random.random() * 10000000000,
                "yearly_change": random.random(),
                "net_change": random.random() * 100000000,
                "density": random.random() * 10000,
                "land_area": random.random() * 10000000,
                "migrants_net": (random.random() * 1000000) + random.random(),
                "fert_rate": (random.random() * 10) + random.random(),
                "med_age": random.random() * 100,
                "urban_pop": random.random() * 100,
                "world_share": (random.random() * 10) + random.random() }

    # Inserting a field dedicated for date edition
    insertion = db["liste"].insert_one(mydict)

    db["liste"].update({"name_country": country}, { "$set" : { "edit_date": str(date.today())}}, False, True)

    # Displaying the new country
    for land in db.liste.find({"name_country": country},{ "_id": 0, }):
        countryContent = land  

    return jsonify(countryContent)

# Search and class country about density
# Distribution:
# - Between 0 and 99 : Small
# - Between 100 and 999 : Medium
# - Between 10000 and 9999 : High
# - 10000 and more : Very high
@app.route('/api/countrydensityselection/', methods =["GET"]) 
def country_density():

    for x in db.liste.find({},{ "_id": 0}):
        
        try:
            value = int(x['density'])
            if (value > 0 and value < 100):
                density_category["Small"].append(x['name_country'])
            elif (value > 100 and value < 999):
                density_category["Medium"].append(x['name_country'])
            elif (value > 1000 and value < 9999):
                density_category["High"].append(x['name_country'])
            elif (value >= 10000):
                density_category["Very high"].append(x['name_country'])
        except:
            logging.warning('excepted')

    return jsonify(density_category)

if __name__ == "__main__":
    app.run()