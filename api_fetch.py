
import requests

API_URL = "https://countries.dev/countries"
TIMEOUT = 15


def fetch_countries():
    """Fetch countries from the API and return a list of dictionaries."""

    try:
        response = requests.get(API_URL, timeout=TIMEOUT)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout:
        print("Error: The API request timed out.")

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API.")

    except requests.exceptions.HTTPError as error:
        print(f"Error: HTTP request failed: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Error: Request failed: {error}")

    except ValueError:
        print("Error: The API returned invalid JSON.")

    return []
