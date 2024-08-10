from flask import Blueprint, jsonify
from .data_processor import fetch_data, process_data

main = Blueprint('main', __name__)

storage = {}  # In-memory storage

@main.route('/fetch-data', methods=['GET'])
def fetch_data_endpoint():
    data = fetch_data()
    processed_data = process_data(data)
    storage['processed_data'] = processed_data
    return jsonify({'message': 'Data fetched and processed'}), 200

@main.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    if 'processed_data' not in storage:
        return jsonify({'message': 'No processed data available'}), 404
    return jsonify(storage['processed_data']), 200
