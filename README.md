# Data Processing Application

## Overview

This Flask application simulates a simplified data retrieval and processing system. It provides endpoints to fetch mock data, process it, and retrieve the processed data.

## Features

1. **`GET /fetch-data`**: Simulates data retrieval from an external service (mock data) and processes the data. The processed data is stored in temporary in-memory storage.
2. **`GET /get-processed-data`**: Retrieves the processed data from in-memory storage. Returns a 404 error if no processed data is available.

## Requirements

- Python 3.7 or higher
- Flask 2.3.0

## Setup and Running Locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/data_processing_app.git
cd data_processing_app

2. Create and Activate a Virtual Environment
Create a virtual environment to manage dependencies:

python3 -m venv venv
Activate the virtual environment:

On macOS and Linux:
source venv/bin/activate

On Windows:
venv\Scripts\activate

3. Install Dependencies
Install the required Python packages:

pip install -r requirements.txt

4. Run the Flask Application
Set the FLASK_APP environment variable and start the Flask development server:

On macOS and Linux:
export FLASK_APP=app
flask run

On Windows:
set FLASK_APP=app
flask run

The application will be available at http://127.0.0.1:5000/.

Endpoints
GET /fetch-data: Fetches and processes mock data. Stores the processed data in memory. Response Example:

json
{
  "message": "Data fetched and processed"
}

GET /get-processed-data: Retrieves the processed data stored in memory. If no processed data is available, returns a 404 error with the following response:

{
  "message": "No processed data available"
}

Troubleshooting

Ensure that you have activated the virtual environment before running the application.

Verify that all dependencies are installed correctly. You can do this by running:

pip list

If the Flask server encounters issues, check the error messages in the terminal for details.

Additional Notes
Mock Data: The /fetch-data endpoint generates a list of 10 random integers between 1 and 100.
Data Processing: The /fetch-data endpoint converts these integers to their string representations and converts them to uppercase.