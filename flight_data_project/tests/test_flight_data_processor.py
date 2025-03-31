import unittest


import sys
import os

# Add the 'src' directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from flight_data_processor import FlightDataProcessor


class TestFlightDataProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = FlightDataProcessor([
            {"flight_number": "AZ001", "departure_time": "2025-02-19 15:30", "arrival_time": "2025-02-20 03:45", "status": "ON_TIME", "duration_minutes": 735},
            {"flight_number": "AZ002", "departure_time": "2025-02-21 11:00", "arrival_time": "2025-02-21 16:00", "status": "DELAYED", "duration_minutes": 300},
        ])
    
    def test_add_flight(self):
        new_flight = {"flight_number": "AZ003", "departure_time": "2025-02-22 10:00", "arrival_time": "2025-02-22 14:30", "status": "ON_TIME"}
        self.processor.add_flight(new_flight)
        self.assertEqual(len(self.processor.flights), 3)
    
    def test_remove_flight(self):
        self.processor.remove_flight("AZ001")
        self.assertEqual(len(self.processor.flights), 1)
    
    def test_flights_by_status(self):
        delayed_flights = self.processor.flights_by_status("DELAYED")
        self.assertEqual(len(delayed_flights), 1)
    
    def test_get_longest_flight(self):
        longest_flight = self.processor.get_longest_flight()
        self.assertEqual(longest_flight['flight_number'], "AZ001")
    
    def test_update_flight_status(self):
        self.processor.update_flight_status("AZ001", "CANCELLED")
        flight = next(f for f in self.processor.flights if f['flight_number'] == "AZ001")
        self.assertEqual(flight['status'], "CANCELLED")
    
if __name__ == "__main__":
    # unittest.main()
    result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestFlightDataProcessor))

   # Print test results
    passed_tests = result.testsRun - len(result.errors) - len(result.failures)
    print(f"Passed: {passed_tests}")
    print(f"Failed: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
