from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db_config = {
    'user': 'root',
    'password': 'n<kEq77&',
    'host': '127.0.0.1',
    'database': 'fuu'
}

@app.route('/')
def home():
    conn = None
    cursor = None
    results = []
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM atulk")
        results = cursor.fetchall()
        print(results)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return render_template('index.html', data=results)

if __name__ == '__main__':
    app.run(debug=True)