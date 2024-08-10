import random

def fetch_data():
    try:
        # Mock data
        return [random.randint(1, 100) for _ in range(10)]
    except Exception as e:
        raise RuntimeError(f"Failed to fetch data: {str(e)}")

def process_data(data):
    try:
        # converting numbers to their string representations and uppercase
        if not isinstance(data, list):
            raise TypeError("Data should be a list")
        return [str(d).upper() for d in data]
    except Exception as e:
        raise RuntimeError(f"Data processing failed: {str(e)}")
