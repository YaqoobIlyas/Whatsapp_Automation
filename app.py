from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app) 
submitted_data = None

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

if __name__ == '__main__':
    print("Server is running in local mode. Ready to accept requests!")  
    app.run(debug=True)
