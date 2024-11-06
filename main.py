# Import the Required modules

# Regular expression module
import re
import pandas as pd
from datetime import datetime

# Import MongoClient to move the pandas df to mongoDB
import pymongo
from pymongo import MongoClient

# Work with PostgresSQL
import psycopg2

with open("mbox.txt") as logs:
    log_file = logs.read()

print(log_file)

# Regular expression to match email addresses in the "From" field
email_pattern = r"From\s+([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})"

# Regular expression to match date in the form --> Day Month  date hh:mm:ss yyyy
date_pattern = (r"From\s+[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\s+([A-Za-z]{3}\s+[A-Za-z]{3}\s+\d{1,"
                r"2}\s+\d{2}:\d{2}:\d{2}\s+\d{4})")

# Find all matches
emails = re.findall(email_pattern, log_file)
dates = re.findall(date_pattern, log_file)

# Convert dates to datetime objects
dates = [datetime.strptime(date, "%a %b %d %H:%M:%S %Y") for date in dates]

# Create a Pandas DataFrame
logs_df = pd.DataFrame({
    "Email": emails,
    "Date": dates
})

# Display the resulting DataFrame
print(logs_df)

# Move the Dataframe to MongoDB

client = MongoClient("mongodb://localhost:27017/")
db = client["log_data_guvi"]
collection = db["user_history"]
mongo_log = logs_df.to_dict(orient="records")
collection.insert_many(mongo_log)

print(f"Inserted {len(mongo_log)} documents into the 'user_history' collection.")

# Verification step
print(collection.find_one())

# Move the data from MongoDB to PostgresSQL
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["log_data_guvi"]
collection = db["user_history"]

mongo_data = list(collection.find())

# Convert the data to a DataFrame
mongo_df = pd.DataFrame(mongo_data)

# Connect to PostgreSQL
postgres_host = "localhost"
postgres_dbname = "server_logs"
postgres_user = "postgres"
postgres_password = "sqltrainer"

conn = psycopg2.connect(
    host=postgres_host,
    dbname=postgres_dbname,
    user=postgres_user,
    password=postgres_password
)
cursor = conn.cursor()
insert_query = '''INSERT INTO user_history (email, date) VALUES (%s, %s);'''

for index, row in mongo_df.iterrows():
    cursor.execute(insert_query, (row['Email'], row['Date']))

conn.commit()

cursor.close()
conn.close()

print("Data has been inserted into PostgreSQL successfully!")

