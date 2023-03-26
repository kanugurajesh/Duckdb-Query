# This file is used to query the data from the firestore database

# importing the required libraries
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd
import duckdb
from fastapi import FastAPI, Request
import json

# Use a service account and add you firebase admin sdk json file
cred = credentials.Certificate("./reastapi-firebase-adminsdk-rby00-97aeff0c91.json")

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred)

# Create a connection to the database
db = firestore.client()

# get the data from the firestone
users_ref = db.collection('users')

# Get the data from the collection
docs = users_ref.stream()

# Convert the data to a list
data = [doc.to_dict() for doc in docs]

# Convert the data to a Pandas DataFrame
df = pd.DataFrame(data)

# Write the data to DuckDB
conn = duckdb.connect(':memory:')

# Create a table called users
conn.register('combined_data', df)

# create a fastapi app
app = FastAPI()

# basic query
basic_query = "SELECT * FROM combined_data WHERE "

# function to add the query to the basic query
def parser(key,value):
    # accessing the global query variable
    global basic_query
    # Checking if the operator is between or not
    if value['operator'] == 'BETWEEN':
        basic_query += f"{key} {value['operator']} '{value['value'][0]}' AND '{value['value'][1]}' AND "
    else:
        basic_query += f"{key} {value['operator']} '{value['value']}' AND "

    return basic_query

# root route and displaying JSON spec
@app.get("/")
async def root():
    with open('example.json', 'r') as f:
        data = json.load(f)
    return data

# using post request for security
@app.post("/query")
async def query(request:Request):

    # waiting for the request to be received
    data = await request.json()

    # assinging the fields to the data variable
    data = data[1]['fields']

    # looping through the data and adding the query to the query variable
    for key,value in data.items():
        parser(key,value)

    # removing the last AND from the query
    basic = basic_query[:-5]
    
    # executing the query and returning the result as JSON
    return conn.execute(basic).fetchdf().to_json(orient='records')