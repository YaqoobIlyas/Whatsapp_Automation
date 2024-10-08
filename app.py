from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Using a dictionary to store data to handle multiple requests
storage = {}

@app.route('/')
def index():
    return "Welcome to the WhatsApp Automation API. Use /data to send a message."

@app.route('/submit', methods=['POST'])
def submit_data():
    global storage  # Access the global dictionary
    data_id = 'last_submitted_data'  # Key for storing the data
    storage[data_id] = request.json  # Store the received data in the dictionary

    print("Received data:", storage[data_id])
    return jsonify({"message": "Data received successfully!", "data": storage[data_id]}), 200

@app.route('/data', methods=['GET'])
def get_data():
    data_id = 'last_submitted_data'  # Key to retrieve the data
    if data_id in storage:
        return jsonify({"data": storage[data_id]}), 200  
    else:
        print("No data received yet.")  
        return jsonify({"message": "No data received yet."}), 404