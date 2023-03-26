# importing the required modules
import pandas as pd
import sqlite3 as sql

# Connect to the database
conn = sql.connect('database.db')

# Read the data from the CSV files
user_data = pd.read_csv('datasets/user_attributes.csv')
event_data = pd.read_csv('datasets/event_attributes.csv')

# Merge the two data frames based on the "user_id" column
combined_data = pd.merge(user_data, event_data, on='user_id')

# Write the combined data to the database
combined_data.to_sql('combined_data', conn, if_exists='replace', index=False)

# Close the connection
conn.close()