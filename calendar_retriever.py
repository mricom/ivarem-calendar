import requests
import json
from datetime import datetime
# Define the endpoint URL
url = "https://diftar.ivarem.be/ophaalkalender/GetOphaaldata"

# Define the request payload
payload = {
    "zipcodeId": "2800-12025",
    "streetId": "https://data.vlaanderen.be/id/straatnaam-10767",
    "housNr": "32",
    "straat": "Leopoldstraat",
    "gemeente": "MECHELEN",
    "fromDate": "2025-01-01T23:00:00.000Z",
    "untilDate": "2025-12-31T23:00:00.000Z"
}

# Set headers (if required, adjust according to API specifications)
headers = {
    "Content-Type": "application/json"
}
def get_calendar_data_from_api():
    # Make the POST request
    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)

    # Print the response
    if response.status_code == 200:
        try:
            data = response.json()

            print("Parsed response:")
            for item in data:
                item['ophaaldatum'] = datetime.fromisoformat(item['ophaaldatum'])
                print(f"Date: {item['ophaaldatum']}, Fraction: {item['fractie']}, Code: {item['fractieCode']}, Color: {item['kleurcode']}")
            return data
        except json.JSONDecodeError:
            print("Failed to parse JSON response.")
    else:
        print("Failed with status code:", response.status_code)
        print("Response text:", response.text)