"""Part 1: Publishing a REST API Using FLASK"""

import json
import requests
from flask import Flask

# API key and URL for WMATA incidents
WMATA_API_KEY = "a1af927580ba4c549d1931ef8fa972fa"
INCIDENTS_URL = "https://jhu-intropython-mod10.replit.app/"
headers = {"api_key": WMATA_API_KEY, "Accept": "*/*"}

# Initialize the Flask app
app = Flask(__name__)

# Define a route
@app.route("/incidents/<unit_type>", methods=["GET"])
def get_incidents(unit_type):
    """
    Retrieve incidents based on the specified unit type.
    """
    incidents = []
    response = requests.get(INCIDENTS_URL, headers=headers, timeout=10)
    incidents_data = response.json()

    # Loop through the incidents data
    for incident in incidents_data.get("ElevatorIncidents", []):
        if incident["UnitType"].upper() == unit_type[:-1].upper():
            incident_dict = {
                "StationCode": incident.get("StationCode"),
                "StationName": incident.get("StationName"),
                "UnitName": incident.get("UnitName"),
                "UnitType": incident.get("UnitType")
            }
            incidents.append(incident_dict)

    return json.dumps(incidents)

if __name__ == "__main__":
    app.run(debug=True)
