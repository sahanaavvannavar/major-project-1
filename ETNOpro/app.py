from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

# Mock data
resources = [
    {"id": 1, "name": "Lab 1", "type": "Lab", "capacity": 30, "available": True},
    {"id": 2, "name": "Seminar Hall", "type": "Hall", "capacity": 100, "available": True},
    {"id": 3, "name": "Projector A", "type": "Equipment", "capacity": None, "available": True},
    {"id": 4, "name": "Lab 2", "type": "Lab", "capacity": 25, "available": True}
]

bookings = []

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    if data and data.get('username') == 'admin' and data.get('password') == 'admin':
        return jsonify({"message": "Login successful", "token": "mock-token-123"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/api/resources', methods=['GET'])
def get_resources():
    return jsonify({"resources": resources})

@app.route('/api/book', methods=['POST'])
def book_resource():
    data = request.json
    resource_id = data.get('resource_id')
    # In a real app we'd validate date/time here
    
    # Mark as unavailable (mocking logic)
    for r in resources:
        if str(r['name']) == str(resource_id):
            bookings.append({"resource": r['name'], "date": data.get('date'), "time": data.get('start_time')})
            return jsonify({"message": "Booking successful"}), 200
            
    return jsonify({"message": "Resource not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=3000)
