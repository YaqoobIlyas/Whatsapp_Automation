from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize a variable to store submitted data
submitted_data = None

@app.before_first_request
def print_startup_message():
    print("Server is running in local mode. Ready to accept requests!")

@app.route('/submit', methods=['POST'])
def submit_data():
    global submitted_data  # Use the global variable to store data
    # Get the JSON data from the request
    submitted_data = request.json

    # Print the received data to the console
    print("Received data:", submitted_data)

    # Optionally, send a response back to the client
    return jsonify({"message": "Data received successfully!", "data": submitted_data}), 200

@app.route('/data', methods=['GET'])
def get_data():
    if submitted_data is not None:
        return jsonify({"data": submitted_data}), 200  # Return the submitted data
    else:
        print("No routes have been called yet. No data received.")  # Print statement when no data is available
        return jsonify({"message": "No data received yet."}), 404  # No data received

if __name__ == '__main__':
    app.run(debug=True)
