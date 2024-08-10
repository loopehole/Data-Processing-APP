from flask import Blueprint, jsonify
from .data_processor import fetch_data, process_data

main = Blueprint('main', __name__)

storage = {} # In-memory storage

@main.route('/fetch-data', methods=['GET'])
def fetch_data_endpoint():
    try:
        data = fetch_data()
        if not data:
            raise ValueError("Fetched data is empty")
        processed_data = process_data(data)
        storage['processed_data'] = processed_data
        return jsonify({'message': 'Data fetched and processed'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    try:
        if 'processed_data' not in storage:
            return jsonify({'message': 'No processed data available'}), 404
        return jsonify(storage['processed_data']), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
