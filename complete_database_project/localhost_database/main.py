# importing the required libraries
from fastapi import FastAPI, Request
import duckdb as db
import json

# Create the FastAPI app
app = FastAPI()

# Create a connection to the database
conn = db.connect("database.db")

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