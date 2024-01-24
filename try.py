import pymysql
import random
from datetime import datetime, timedelta
# Connect to the MySQL database
conn = pymysql.connect(host='sql6.freesqldatabase.com', port=3306, user='sql6679460', password='TvM8EaUPTm', database='sql6679460')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a simple query
# cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY, name VARCHAR(255), age INT)''')

# Insert data into the table
names = [
    "Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Henry", "Ivy", "Jack",
    "Kate", "Liam", "Mia", "Noah", "Olivia", "Paul", "Quinn", "Ryan", "Sara", "Tom",
    "Uma", "Victor", "Wendy", "Xander", "Yara", "Zane",
    "Amy", "Benjamin", "Catherine", "Daniel", "Emily", "Felix", "Gemma", "Harrison", "Isabel", "Jacob",
    "Kylie", "Luke", "Megan", "Nathan", "Oscar", "Penelope", "Quentin", "Riley", "Sophia", "Tyler",
    "Ursula", "Vincent", "Willow", "Xavier", "Yasmine", "Zachary"
]
# import random

# List of two-letter country codes
country_codes = ["AF", "AL", "DZ", "AD", "AO", "AG", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "BI", "CV", "KH", "CM", "CA", "CF", "TD", "CL", "CN", "CO", "KM", "CG", "CD", "CR", "HR", "CU", "CY", "CZ", "DK", "DJ", "DM", "DO", "TL", "EC", "EG", "SV", "GQ", "ER", "EE", "ET", "FJ", "FI", "FR", "GA", "GM", "GE", "DE", "GH", "GR", "GD", "GT", "GN", "GW", "GY", "HT", "HN", "HU", "IS", "IN", "ID", "IR", "IQ", "IE", "IL", "IT", "CI", "JM", "JP", "JO", "KZ", "KE", "KI", "KP", "KR", "KW", "KG", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MR", "MU", "MX", "FM", "MD", "MC", "MN", "ME", "MA", "MZ", "MM", "NA", "NR", "NP", "NL", "NZ", "NI", "NE", "NG", "NO", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "QA", "RO", "RU", "RW", "KN", "LC", "VC", "WS", "SM", "ST", "SA", "SN", "RS", "SC", "SL", "SG", "SK", "SI", "SB", "SO", "ZA", "ES", "LK", "SD", "SR", "SZ", "SE", "CH", "SY", "TW", "TJ", "TZ", "TH", "TG", "TO", "TT", "TN", "TR", "TM", "TV", "UG", "UA", "AE", "GB", "US", "UY", "UZ", "VU", "VA", "VE", "VN", "YE", "ZM", "ZW"]

def random_timestamp(start_date, end_date):
    time_delta = end_date - start_date
    random_days = random.randint(0, time_delta.days)
    random_time = timedelta(days=random_days)
    random_datetime = start_date + random_time
    return random_datetime.strftime("%Y-%m-%d %H:%M:%S")

# Example usage
start_date = datetime(2024, 1, 12)
end_date = datetime(2024, 1, 24)

# random_timestamp_value = random_timestamp(start_date, end_date)
# print("Random Timestamp:", random_timestamp_value)


for i in range(1,101):
    random_timestamp_value = random_timestamp(start_date, end_date)
    cursor.execute("INSERT INTO user (uid, name, score, country, timestamp) VALUES (%s, %s, %s, %s, %s)", (i,random.choice(names), random.randint(0, 500),  random.choice(country_codes), random_timestamp_value))

# Commit the changes
conn.commit()

# Execute a SELECT query
cursor.execute("SELECT * FROM user")
rows = cursor.fetchall()

# Display the results
for row in rows:
    print(row)

# Close the connection
conn.close()
