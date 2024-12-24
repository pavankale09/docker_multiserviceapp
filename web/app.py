from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Docker Multi-Service App!"

@app.route('/data')
def get_data():
    try:
        db = mysql.connector.connect(
            host="db",
            user="root",
            password="password",
            database="testdb"
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM sample_table;")
        result = cursor.fetchall()
        return jsonify(result)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
