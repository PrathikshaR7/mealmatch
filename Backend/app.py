from flask import Flask, request, jsonify
import sqlite3
import googlemaps
# from distances import haversine

app = Flask(__name__)

def get_db_connection():
    try:
        conn = sqlite3.connect("C:\\Users\\rakes\\hackathon\\new\\ngofood.db")
        conn.row_factory = sqlite3.Row
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

@app.route('/')
def home():
    conn=get_db_connection()
    if conn is None:
        return "error1",500
    try:
        conn.execute('DELETE from ngo_details WHERE LOWER("del") NOT LIKE LOWER("%bengaluru%") and LOWER("del") NOT LIKE LOWER("%bangalore")')
        ngos = conn.execute('SELECT * from ngo_details').fetchall()
        conn.close()
        
    except Exception as e:
        return "error2",500
    ngos_list=[dict(row) for row in ngos]
    return jsonify(ngos_list)

@app.route('/new')
def new():
    conn=get_db_connection()
    if conn is None:
        return "error1",500
    try:
        ngos = conn.execute('SELECT * from ngo_details').fetchall()
        conn.close()
    except Exception as e:
        return "error2",500
    ngos_list=[dict(row) for row in ngos]
    return jsonify(ngos_list)

@app.route('/pincode', methods=['POST'])
def get_by_pincode():
    conn = get_db_connection()
    if conn is None:
        return "error1", 500
    
    # Get the pincode from the request
    pincode = request.json.get('pincode')
    if not pincode:
        return jsonify({"error": "Pincode is required"}), 400
    
    try:
        # Query for NGOs matching the pincode
        ngos = conn.execute('SELECT * FROM ngo_details WHERE pincode = ?', (pincode,)).fetchall()
        conn.close()
    except Exception as e:
        return "error2", 500
    
    ngos_list = [dict(row) for row in ngos]
    return jsonify(ngos_list)

if __name__ == '__main__':
    app.run(debug=True)