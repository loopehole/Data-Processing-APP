import random

def fetch_data():
    # Mock data simulating fetched data
    return [random.randint(1, 100) for _ in range(10)]

def process_data(data):
    # Convertinng numbers to their string representations and uppercase
    return [str(d).upper() for d in data]
