import ipaddress # Library to check IP validity.
from flask import Flask, request, jsonify # Library for Web frameworks (app object, incoming request data and JSON responses).
from flask_cors import CORS # Handles Cross-Origin requests (lets GitHub Pages call API).
import os # Access environment variables (e.g. the API key).
from dotenv import load_dotenv # Loads .env values into environment variables.
import requests # Makes the HTTP call out to the VirusTotal API.
# gunicorn # Package used to run app on render (external server) Placed on requirements file but not needed in python code. 

"""
Flask web application exposing an API endpoint that checks the reputation of an
IP address via the VirusTotal API. It validates the submitted IP address,
queries VirusTotal, and returns a JSON response with the analysis results,
with error handling for invalid input, API request failures, and missing data
in the API response.

Deployment (Render):
- Hosted as a Render Web Service, connected to this GitHub repo; pushes to the
  linked GitHub branch triggering an automatic rebuild and deploy.
- Dependencies are installed from requirements.txt (Flask, requests,
  python-dotenv, gunicorn).
- API_KEY is set as an environment variable in the Render dashboard
  (Environment tab) rather than committed in a .env file.
- CORS is configured to allow requests from the frontend's origin
  (the GitHub Pages site).

Local development:
- Install dependencies: `pip install -r requirements.txt`
- Provide API_KEY in a local .env file (loaded by python-dotenv).
- Run with `python app.py` (Flask's dev server) or `gunicorn app:app`.
"""

# ------ Variables set for python code ------

load_dotenv()

api_key = os.getenv("API_KEY") # Setting API key as a variable.
if not api_key:
    raise ValueError("API key is not set.") # Error if no API key found.

vt_api_url = "https://www.virustotal.com/api/v3/ip_addresses"
app_origin = {
    "http://127.0.0.1:5500",                 # Local live server.
    "https://jp3379a-nulondon.github.io",    # GitHub Pages.
}
request_timeout = 6  # Request timeout in seconds 

# Specific header that VirusTotal's API requires for authentication
HEADERS = {
    "Accept": "application/json",
    "x-apikey": api_key,
}

# Creates Flask web application object.
app = Flask(__name__) 


# ------ Flask CORS headers needed for live server ------

@app.after_request  # Runs automatically after every request
def add_cors_headers(response):
    """Function that lets GitHub Pages connect to Render backend without the browser blocking it. 
    
    Only approved origins on allowed list work.
    """
    origin = request.headers.get("Origin")
    if origin in app_origin:
        response.headers["Access-Control-Allow-Origin"] = origin
    response.headers["Access-Control-Allow-Headers"] = "Content-Type" # Allows the browser to send a Content-Type header needed for JSON
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS" # Tells the browser which HTTP methods are accepted
    return response


# --- Functions for IP validation and handing data  ------

def valid_ip(ip_address):
    """Returns "True" if the string is a valid IPv4 or IPv6 address.
    
    Error is raise if not a correctly fomratted IP address.
    """
    try:
        ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        return False


def fetch_ip_data(ip_address):
    """Call VirusTotal API and return the parsed full JSON result.
    
    Raises a HTTP status code error or timeout error if applicable. 
    """
    response = requests.get(
        f"{vt_api_url}/{ip_address}",
        headers=HEADERS,
        timeout=request_timeout,
    )
    response.raise_for_status()
    return response.json()


def extract_stats(ip_address, ip_data):
    """Pull the analysis summary out of the VirusTotal response.

    Raises KeyError if the expected fields are missing.
    """
    stats = ip_data["data"]["attributes"]["last_analysis_stats"]
    return {
        "ip_address": ip_address,
        "malicious": stats.get("malicious", 0),
        "suspicious": stats.get("suspicious", 0),
        "undetected": stats.get("undetected", 0),
        "harmless": stats.get("harmless", 0),
    }


def error_response(message, status):
    """JSON error response."""
    return jsonify({"success": False, "error": message}), status


# ------ Application route deploying functions ------

@app.route("/api/ip-reputation", methods=["POST", "OPTIONS"])
def ip_reputation():
    """Handle an IP reputation lookup request.

    This is the main API endpoint. It accepts a POST with a JSON body e.g.
    {"ip_address": "8.8.8.8"}, validates the address, looks it up on
    VirusTotal, and returns a JSON response.

    On success: {"success": True, "results": {...}}
    On failure: {"success": False, "error": "..."} with an HTTP status code.
    """
    
    # OPTIONS call made to check Flask CORS.
    if request.method == "OPTIONS":
        return "", 204

    # JSON body turned into varibale 'data'.
    data = request.get_json(silent=True)

    # Checks user request - Rejects request if nothing is submitted.
    if not data or not data.get("ip_address"):
        return error_response("No IP address was provided.", 400)

    # Checks user request - Rejects request if IP is not correctly formatted
    user_ip = data["ip_address"].strip()
    if not valid_ip(user_ip):
        return error_response(
            "Invalid IP address. Enter a correctly formatted IP address.", 400
        )

    try:
        ip_data = fetch_ip_data(user_ip)
        results = extract_stats(user_ip, ip_data) # Gathers required information 

    # Reply from VirusTotal API - Bad status
    except requests.HTTPError as error: 
        status = error.response.status_code     
        return error_response(
            f"VirusTotal request failed ({status}). "
            "Check your API key, the IP, or your request limit.", # Personal API keys have a limit of 4 requests a minute
            502,
        )
    
    # The response was missing expected fields (KeyError) or wasn't valid JSON (ValueError).
    except (KeyError, ValueError):
        return error_response(
            "Could not find analysis data in the VirusTotal response.", 502
        )
    
     # Never reached VirusTotal (no connection, DNS issue, or timeout).
    except requests.RequestException as error:
        return error_response(f"Could not reach VirusTotal: {error}", 502)

    # Results are sent back as a JSON.
    return jsonify({"success": True, "results": results})


if __name__ == "__main__":
    app.run()  # add debug=True only for local development
