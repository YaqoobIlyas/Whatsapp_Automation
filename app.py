from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt  
import re  
import os

app = Flask(__name__)
CORS(app)
SECRET_KEYs = os.environ.get('SECRET_KEY')
storage = None

def verify_jwt(token):
    try:
        decoded = jwt.decode(token, SECRET_KEYs, algorithms=['HS256'])
        return decoded
    except jwt.ExpiredSignatureError:
        print("JWT token has expired.")
        return None
    except jwt.InvalidTokenError as e:
        print("JWT Error:", e)
        return None


def validate_phone_number(phone_number):

    if re.fullmatch(r'\d{10}', phone_number):
        return  phone_number  
    return None

@app.route('/')
def index():
    return "Welcome to the WhatsApp Automation API. Use /submit to send a message."

@app.route('/submit', methods=['POST'])
def submit_data():
    global storage

    #token = request.headers.get('Authorization')

    #if not token or not token.startswith('Bearer '):
     #   return jsonify({"message": "Missing or invalid token!"}), 401

   # token = token.split(" ")[1]
   # decoded_token = verify_jwt(token)
   # if not decoded_token:
   #     return jsonify({"message": "Unauthorized access!"}), 401

    incoming_data = request.json
    if not incoming_data:
        return jsonify({"message": "No data provided!"}), 400

    phone_number = incoming_data.get("phone_number")
    message = incoming_data.get("message")

    if not phone_number or not message:
        return jsonify({"message": "Phone number or message cannot be null!"}), 400

    validated_phone_number = validate_phone_number(phone_number)
    if not validated_phone_number:
        return jsonify({"message": "Invalid phone number. It must be exactly 10 digits!"}), 400

    storage = {"phone_number": validated_phone_number, "message": message}
    
    return jsonify({"message": "Data pushed"}), 200

@app.route('/data', methods=['GET'])
def get_data():
    global storage

    if storage is not None:
        data_to_return = storage
        storage = None
        return jsonify({"data": data_to_return}), 200
    else:
        print("No data received yet.")
        return jsonify({"message": "No data received yet."}), 404

