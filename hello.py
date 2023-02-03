import requests

def get-response() -> int:
    return requests.get('https://www.google.com/').status_code
