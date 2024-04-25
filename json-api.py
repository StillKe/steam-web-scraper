import json
import requests

# Prompt the user to enter the URL
url = input("Enter the URL you want to scrape: ")

try:
    # Send a GET request to the URL provided by the user
    r = requests.get(url)
    print("Response status code:", r.status_code)  # Print status code for debugging
    r.raise_for_status()  # Raise an exception for bad status codes
    print("Response content:", r.text)  # Print response content for debugging
    data = r.json()  # Automatically parse JSON response
    print("Parsed JSON data:", data)  # Print parsed JSON data for debugging
except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
