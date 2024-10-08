from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app) 
submitted_data = None

@app.route('/')
def index():
    return "Welcome to the WhatsApp Automation API. Use /data to send a message."

@app.route('/submit', methods=['POST'])
def submit_data():
    global submitted_data  
 
    submitted_data = request.json
 
    print("Received data:", submitted_data)
    return jsonify({"message": "Data received successfully!", "data": submitted_data}), 200

@app.route('/data', methods=['GET'])
def get_data():
    if submitted_data is not None:
        return jsonify({"data": submitted_data}), 200  
    else:
        print("No routes have been called yet. No data received.")  
        return jsonify({"message": "No data received yet."}), 404  


