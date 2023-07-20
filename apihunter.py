#!/usr/bin/python3
# coding: utf-8

import requests

def capture_api_from_url(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            # If the request was successful (status code 200), you can access the response data
            # using response.text for text-based data or response.json() for JSON data.
            # For example, if the response is in JSON format:
            data = response.json()

            # Process the data as needed
            print("API captured successfully:")
            print(data)
        else:
            print(f"Failed to capture API. Status Code: {response.status_code}")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'YOUR_API_URL' with the actual URL you want to capture data from.
    api_url = "YOUR_API_URL"
    capture_api_from_url(api_url)

