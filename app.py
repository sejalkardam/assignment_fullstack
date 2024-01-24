import datetime
from datetime import datetime, timedelta 
from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# MySQL Workbench connection details
db_config = {
    'user': 'sql6679460',
    'password': 'TvM8EaUPTm',
    'host': 'sql6.freesqldatabase.com',
    'database': 'sql6679460',
    'raise_on_warnings': True
}

# Create a MySQL connection
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Function to execute a MySQL query and fetch results
def execute_query(query, params=None, fetchone=False):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute(query, params)
        if fetchone:
            result = cursor.fetchone()
        else:
            result = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

    return result

# Display current week leaderboard (Top 200)
@app.route('/leaderboard/current_week', methods=['GET'])
def current_week_leaderboard():
    start_date = datetime.now() - timedelta(days=datetime.now().weekday())
    query = "SELECT * FROM user WHERE timestamp >= %s ORDER BY score DESC LIMIT 200"
    params = (start_date,)
    leaderboard = execute_query(query, params)
    return jsonify(leaderboard)

# Display last week leaderboard for a given country (Top 200)
@app.route('/leaderboard/last_week', methods=['GET'])
def last_week_leaderboard():
    country_code = request.args.get('country_code')
    # country_code = 'DK'
    if not country_code:
        return jsonify({'error': 'Country code is required'}), 400

    end_date = datetime.now() - timedelta(days=datetime.now().weekday() + 7)
    start_date = end_date - timedelta(days=6)
    print(f"start_date: {start_date}, end_date: {end_date}, country_code: {country_code}")

    query = "SELECT * FROM assignment.user WHERE timestamp BETWEEN %s AND %s AND country = %s ORDER BY score DESC LIMIT 200"


    # query = "SELECT * FROM assignment.user WHERE timestamp >= %s AND timestamp <= %s AND country = %s ORDER BY score DESC LIMIT 200"
    params = (start_date, end_date, country_code)
    leaderboard = execute_query(query, params)
    return jsonify(leaderboard)

# Fetch user rank by UID
@app.route('/leaderboard/user_rank', methods=['GET'])
def user_rank():
    uid = request.args.get('uid')
    print(f"Received UID: {uid}")
    if not uid:
        return jsonify({'error': 'User ID is required'}), 400

    # query = "SELECT `RANK`() OVER (ORDER BY score DESC) AS rank FROM leaderboard WHERE uid = %s"
    query = """
    SELECT 
        (SELECT COUNT(*) + 1
         FROM assignment.user AS l2
         WHERE l2.score > l1.score) AS user_rank
    FROM assignment.user AS l1
    WHERE uid = %s
"""

    params = (uid,)
    result = execute_query(query, params, fetchone=True)

    if result:
        return jsonify({'user_rank': result['user_rank']})
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')



# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run(debug=True)
