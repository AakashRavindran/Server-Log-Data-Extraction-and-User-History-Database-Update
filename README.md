# Email Log Data Processing and Analysis

This project processes and analyzes email log data using multiple technologies such as Python, MongoDB, PostgreSQL, and Streamlit. The process involves:

1. Extracting email addresses and dates from a log file.
2. Storing the extracted data into MongoDB.
3. Transferring the data from MongoDB to PostgreSQL.
4. Performing SQL queries to analyze the data and display the results in a Streamlit application.

## Project Structure

- `main.py`: Main script to extract email addresses and dates from a log file, move data to MongoDB, and then to PostgreSQL.
- `get_sql_data.py`: Contains SQL queries to analyze the data stored in PostgreSQL, and the results are displayed using Streamlit.

## Technologies Used

- **Python** for scripting.
- **pandas** for data manipulation.
- **MongoDB** for NoSQL storage.
- **PostgreSQL** for relational database storage and analysis.
- **Streamlit** for data visualization.

## Requirements / Modules used

Make sure to have the following installed on your local machine:

- Python 3.x
- MongoDB server
- PostgreSQL server
- Required Python libraries:
  - `pandas`
  - `pymongo`
  - `psycopg2`
  - `streamlit`
  - `sqlalchemy`

You can install the required Python libraries using pip:

```bash
pip install pandas pymongo psycopg2 streamlit sqlalchemy

**## 1. Prepare MongoDB and PostgreSQL**
Make sure you have MongoDB and PostgreSQL set up and running locally. You'll need to create a PostgreSQL database (server_logs) and a MongoDB collection (user_history) where the email log data will be inserted.

**## 2. Run the Main Script (main.py)**
The main.py script does the following:

Reads the email log file (mbox.txt).
Uses regular expressions to extract email addresses and dates from the log file.
Converts the data into a pandas DataFrame.
Inserts the DataFrame into MongoDB (log_data_guvi database, user_history collection).
Transfers the data from MongoDB to PostgreSQL.

**## 3. SQL Queries and Data Analysis (get_sql_data.py)**
The get_sql_data.py script executes various SQL queries on the PostgreSQL database (server_logs), performs data analysis, and displays the results via Streamlit.

To run the Streamlit app:

bash
Copy code
streamlit run get_sql_data.py

SQL Queries Performed
1.List all unique email addresses
2.Count the number of emails received per day
3.Find the first and last email date for each email address
4.Count the total number of emails from each domain
5.Find the email address with the most emails received
6.Find the number of emails received in the year 2008
7.Find the email addresses that received emails on both January 5 and January 6, 2008
8.Get the total number of emails received for each month in 2008
9.List the domains that sent the most emails
10.Find the total number of emails received after January 5, 2008
11.Find the most active days of the week
12.Get the number of emails received by each domain in 2008
13.Find the average number of emails received per email address in 2008
14.Find email addresses that received more than 100 emails in total

