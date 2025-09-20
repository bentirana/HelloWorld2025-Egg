import requests
import json

# Define the endpoint URL
url = "https://api.hfs.purdue.edu/menus/v2/locations/Hillenbrand/2025-09-21"

def fetch_and_convert() -> dict:
    try:
        # Fetch the JSON data from the endpoint
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP issues

        # Print the Content-Type of the response
        print("Content-Type:", response.headers.get("Content-Type"))

        # Load the JSON data
        json_data = response.json()

        # Convert the JSON data to a formatted string for readability
        json_string = json.dumps(json_data, indent=4)

        # Print the formatted JSON data
        print(json_string)

        # Optionally, save the JSON data to a file
        with open("output.json", "w") as json_file:
            json_file.write(json_string)

        return json_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except Exception as e:
        print(f"Error processing data: {e}")

if __name__ == "__main__":
    print(fetch_and_convert()["Meals"][0]["Name"])
    print(fetch_and_convert()["Location"])