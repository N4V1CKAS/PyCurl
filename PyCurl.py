import requests
import sys

url = input("Enter your URL: ")

try:
    req = requests.get(url)
    print(req.status_code)
    print(req.text[:500])
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
