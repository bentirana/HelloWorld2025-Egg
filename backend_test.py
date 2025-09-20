import asyncio
import requests
import json
from datetime import date

async def fetch_and_convert(location: str, date: date) -> dict:
    url = f'https://api.hfs.purdue.edu/menus/v2/locations/{location}/{date.strftime("%Y-%m-%d")}'
    # print(date.strftime("%Y-%m-%d"))

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
        # print(json_string)

        # Optionally, save the JSON data to a file
        with open("output.json", "w") as json_file:
            json_file.write(json_string)

        return json_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except Exception as e:
        print(f"Error processing data: {e}")

def main():
    data = fetch_and_convert()
    print(data["Location"])

if __name__ == "__main__":
    main()