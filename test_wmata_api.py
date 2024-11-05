"""Part 2: Creating Unit Tests for Manual Execution"""

import json
import unittest
from wmata_api import app

class WMATATest(unittest.TestCase):
    """
    Unit tests for the WMATA functionalities.
    """
    def test_http_success(self):
        """
        Test that the HTTP response for the escalator endpoint is successful (status code 200).
        """
        # Test the /incidents/escalators endpoint for a 200 status code
        escalator_response = app.test_client().get('/incidents/escalators')
        self.assertEqual(escalator_response.status_code, 200,
                         "Escalators endpoint did not return status 200")

        # Test the /incidents/elevators endpoint for a 200 status code
        elevator_response = app.test_client().get('/incidents/elevators')
        self.assertEqual(elevator_response.status_code, 200,
                         "Elevators endpoint did not return status 200")

    # Ensure all returned incidents have the 4 required fields
    def test_required_fields(self):
        """
        Test that all returned incidents have the required fields
        """
        required_fields = ["StationCode", "StationName", "UnitType", "UnitName"]
        response = app.test_client().get('/incidents/escalators')
        json_response = json.loads(response.data.decode())

        # Check that each incident contains all required fields
        for incident in json_response:
            for field in required_fields:
                self.assertIn(field, incident, f"Missing required field {field} in response")

    def test_escalators(self):
        """
        Test that all entries returned by the /incidents/escalators endpoint 
        have a UnitType of "ESCALATOR".
        """
        response = app.test_client().get('/incidents/escalators')
        json_response = json.loads(response.data.decode())

        for incident in json_response:
            self.assertEqual(incident.get("UnitType"), "ESCALATOR",
                             "UnitType is not 'ESCALATOR' for /incidents/escalators")

    def test_elevators(self):
        """
        Test that all entries returned by the /incidents/elevators endpoint 
        have a UnitType of "ELEVATOR".
        """
        response = app.test_client().get('/incidents/elevators')
        json_response = json.loads(response.data.decode())

        for incident in json_response:
            self.assertEqual(incident.get("UnitType"), "ELEVATOR",
                             "UnitType is not 'ELEVATOR' for /incidents/elevators")

if __name__ == '__main__':
    unittest.main()
