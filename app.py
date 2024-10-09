from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

storage = None

@app.route('/')
def index():
    return "Welcome to the WhatsApp Automation API. Use /data to send a message."

@app.route('/submit', methods=['POST'])
def submit_data():
    global storage  
    storage = request.json  # Store the incoming data

    print("Received data:", storage)
    return jsonify({"message": "Data received successfully!", "data": storage}), 200

@app.route('/data', methods=['GET'])
def get_data():
    global storage  # Use the global storage variable

    if storage is not None:
        data_to_return = storage  # Save the current data to return to the requester
        storage = None  # Reset the storage so the data is not available for the next request
        return jsonify({"data": data_to_return}), 200  
    else:
        print("No data received yet.")  
        return jsonify({"message": "No data received yet."}), 404