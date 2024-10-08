from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_data():
    # Get the JSON data from the request
    data = request.json

    # Print the received data to the console
    print("Received data:", data)

    # Optionally, send a response back to the client
    return jsonify({"message": "Data received successfully!", "data": data}), 200

if __name__ == '__main__':
    app.run(debug=True)
