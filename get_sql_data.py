import pandas as pd
from sqlalchemy import create_engine
import streamlit as st

pd.set_option("display.max_columns", 120)
pd.set_option("display.max_rows", 120)

postgres_user = "postgres"
postgres_password = "sqltrainer"
postgres_host = "localhost"
postgres_port = "5432"
postgres_db = "server_logs"

engine = create_engine(
    f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}")

st.title("GUVI Email LOG Data Analysis")

# 1. List all unique email addresses
query1 = "SELECT DISTINCT email FROM user_history;"
result_df1 = pd.read_sql_query(query1, con=engine)
st.subheader("1. List all unique email addresses")
st.write(result_df1)

# 2. Count the number of emails received per day
query2 = ("SELECT DATE(date) AS email_date, COUNT(*) AS email_count FROM user_history GROUP BY DATE(date) "
          "ORDER BY email_date;")
result_df2 = pd.read_sql_query(query2, con=engine)
st.subheader("2. Count the number of emails received per day")
st.write(result_df2)

# 3. Find the first and last email date for each email address
query3 = """
SELECT email, MIN(date) AS first_email_date, MAX(date) AS last_email_date
FROM user_history
GROUP BY email
ORDER BY email;
"""
result_df3 = pd.read_sql_query(query3, con=engine)
st.subheader("3. Find the first and last email date for each email address")
st.write(result_df3)

# 4. Count the total number of emails from each domain
query4 = """
SELECT SUBSTRING(email FROM '@(.*)') AS domain, COUNT(*) AS email_count
FROM user_history
GROUP BY domain
ORDER BY email_count DESC;
"""
result_df4 = pd.read_sql_query(query4, con=engine)
st.subheader("4. Count the total number of emails from each domain")
st.write(result_df4)

# 5. Find the email address with the most emails received
query5 = """
SELECT email, COUNT(*) AS email_count
FROM user_history
GROUP BY email
ORDER BY email_count DESC
LIMIT 1;
"""
result_df5 = pd.read_sql_query(query5, con=engine)
st.subheader("5. Find the email address with the most emails received")
st.write(result_df5)

# 6. Find the number of emails received in the year 2008
query6 = """
SELECT COUNT(*) AS emails_2008
FROM user_history
WHERE EXTRACT(YEAR FROM date) = 2008;
"""
result_df6 = pd.read_sql_query(query6, con=engine)
st.subheader("6. Find the number of emails received in the year 2008")
st.write(result_df6)

# 7. Find the email addresses that received emails on both January 5 and January 6, 2008
query7 = """
SELECT email
FROM user_history
WHERE DATE(date) IN ('2008-01-05', '2008-01-06')
GROUP BY email
HAVING COUNT(DISTINCT DATE(date)) = 2;
"""
result_df7 = pd.read_sql_query(query7, con=engine)
st.subheader("7. Find the email addresses that received emails on both January 5 and January 6, 2008")
st.write(result_df7)

# 8. Get the total number of emails received for each month in 2008
query8 = """
SELECT EXTRACT(MONTH FROM date) AS month, COUNT(*) AS email_count
FROM user_history
WHERE EXTRACT(YEAR FROM date) = 2008
GROUP BY month
ORDER BY month;
"""
result_df8 = pd.read_sql_query(query8, con=engine)
st.subheader("8. Get the total number of emails received for each month in 2008")
st.write(result_df8)

# 9. List the domains that sent the most emails
query9 = """
SELECT SUBSTRING(email FROM '@(.*)') AS domain, COUNT(*) AS email_count
FROM user_history
GROUP BY domain
ORDER BY email_count DESC
LIMIT 1;
"""
result_df9 = pd.read_sql_query(query9, con=engine)
st.subheader("9. List the domains that sent the most emails")
st.write(result_df9)

# 10. Find the total number of emails received after January 5, 2008
query10 = """
SELECT DISTINCT email
FROM user_history
WHERE date > '2008-01-05';
"""
result_df10 = pd.read_sql_query(query10, con=engine)
st.subheader("10. Find the total number of emails received after January 5, 2008")
st.write(result_df10)


# 11.Find the most active days of the week
query11 = """
SELECT TO_CHAR(date, 'Day') AS day_of_week, COUNT(*) AS email_count
FROM user_history
GROUP BY day_of_week
ORDER BY email_count DESC;
"""
result_df11 = pd.read_sql_query(query11, con=engine)
st.subheader("11.Find the most active days of the week")
st.write(result_df11)

# 12.Get the number of emails received by each domain in 2008.
query12 = """
SELECT SUBSTRING(email FROM '@(.*)') AS domain, COUNT(*) AS email_count
FROM user_history
WHERE EXTRACT(YEAR FROM date) = 2008
GROUP BY domain
ORDER BY email_count DESC;
"""
result_df12 = pd.read_sql_query(query12, con=engine)
st.subheader("12.Find the month with the highest average number of emails per day in 2008.")
st.write(result_df12)


# 13.Find the average number of emails received per email address in 2008.
query13 = """
SELECT AVG(email_count) AS avg_email_per_address
FROM (
    SELECT email, COUNT(*) AS email_count
    FROM user_history
    WHERE EXTRACT(YEAR FROM date) = 2008
    GROUP BY email
) AS email_counts;
"""
result_df13 = pd.read_sql_query(query13, con=engine)
st.subheader("13.Find the average number of emails received per email address in 2008.")
st.write(result_df13)

# 14.Find email addresses that received more than 100 emails in total.
query14 = """
SELECT email, COUNT(*) AS email_count
FROM user_history
GROUP BY email
HAVING COUNT(*) > 100
ORDER BY email_count DESC;
"""
result_df14 = pd.read_sql_query(query14, con=engine)
st.subheader("14.Find email addresses that received more than 100 emails in total.")
st.write(result_df14)

