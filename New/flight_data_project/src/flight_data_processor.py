from typing import List, Dict, Optional
import datetime

class FlightDataProcessor:
    def __init__(self, flights: Optional[List[Dict]] = None) -> None:
        self.flights = flights if flights else []
        for flight in self.flights:
            if 'duration_minutes' not in flight:
                flight['duration_minutes'] = self._calculate_duration(flight['departure_time'], flight['arrival_time'])
    
    def add_flight(self, data: Dict) -> None:
        if not any(flight['flight_number'] == data['flight_number'] for flight in self.flights):
            duration = self._calculate_duration(data['departure_time'], data['arrival_time'])
            data['duration_minutes'] = duration
            self.flights.append(data)
            print(f"Flight {data['flight_number']} added successfully.")
    
    def remove_flight(self, flight_number: str) -> None:
        self.flights = [flight for flight in self.flights if flight['flight_number'] != flight_number]
        print(f"Flight {flight_number} removed successfully.")
    
    def flights_by_status(self, status: str) -> List[Dict]:
        result = [flight for flight in self.flights if flight['status'] == status]
        print(f"Flights with status '{status}': {result}")
        return result
    
    def get_longest_flight(self) -> Optional[Dict]:
        if not self.flights:
            print("No flights available.")
            return None
        longest_flight = max(self.flights, key=lambda flight: flight['duration_minutes'])
        print(f"Longest flight: {longest_flight}")
        return longest_flight
    
    def update_flight_status(self, flight_number: str, new_status: str) -> None:
        for flight in self.flights:
            if flight['flight_number'] == flight_number:
                flight['status'] = new_status
                print(f"Flight {flight_number} status updated to {new_status}.")
                break
    
    @staticmethod
    def _calculate_duration(departure_time: str, arrival_time: str) -> int:
        dep_time = datetime.datetime.strptime(departure_time, "%Y-%m-%d %H:%M")
        arr_time = datetime.datetime.strptime(arrival_time, "%Y-%m-%d %H:%M")
        return int((arr_time - dep_time).total_seconds() / 60)

if __name__ == "__main__":
    flight_data = [
        {"flight_number": "AZ001", "departure_time": "2025-02-19 15:30", "arrival_time": "2025-02-20 03:45", "status": "ON_TIME"},
        {"flight_number": "AZ002", "departure_time": "2025-02-21 11:00", "arrival_time": "2025-02-21 16:00", "status": "DELAYED"}
    ]
    processor = FlightDataProcessor(flight_data)
    processor.add_flight({"flight_number": "AZ003", "departure_time": "2025-02-22 10:00", "arrival_time": "2025-02-22 14:30", "status": "ON_TIME"})
    processor.remove_flight("AZ001")
    processor.flights_by_status("ON_TIME")
    processor.get_longest_flight()
    processor.update_flight_status("AZ002", "CANCELLED")
