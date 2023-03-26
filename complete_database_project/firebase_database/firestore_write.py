# This file is used to write data to the firestore database

# import the necessary packages
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd

# Use a service account and add firestone sdk json file
cred = credentials.Certificate("./app/reastapi-firebase-adminsdk-rby00-97aeff0c91.json")
firebase_admin.initialize_app(cred)

# Load the data from the CSV files
user_data = pd.read_csv('datasets/user_attributes.csv')
event_data = pd.read_csv('datasets/event_attributes.csv')

# merge the data at user id
data = pd.merge(user_data, event_data, on='user_id')

# Convert the data to a dictionary
data = data.to_dict('records')

# Create a connection to the database
db = firestore.client()

# Write the data to the database
for record in data:
    db.collection('users').add(record)