import unittest

class TestSolutionValidity(unittest.TestCase):
    def setUp(self):
        # Data setup for cities and tours:
        self.total_cities = 21  # Including depot
        self.robot_tours = {
            0: [0, 1, 10, 7, 19, 11, 20, 0, 13, 2, 17, 4, 15, 3, 9, 5, 12, 14, 8, 18, 6, 0],
            1: [0, 16, 0]
        }

    def test_unique_visits(self):
        # Test that each city is visited exactly once by one salesman:
        all_visits = []
        for tour in self.robot_tours.values():
            all_visits.extend(tour)
        
        # Check for all cities except the repeated depots (city 0 naturally appears multiple times):
        visits_count = {city: all_visits.count(city) for city in set(all_visits) if city != 0}
        for city_count in visits_count.values():
            self.assertEqual(city_count, 1)
    
    def test_departure_from_depot(self):
        # Check that each robot only starts their tour once exactly from the depot:
        for tour in self.robot_tours.values():
            # Start and end should be the depot:
            self.assertEqual(tour[0], 0, "Tour should start at the depot")
            self.assertEqual(tour[-1], 0, "Tour should end at the depot")

            # Count how many times each robot departs from the depot:
            departures = tour.count(0)
            # As tours are roundtrips, starting and ending at depot, count should be 2
            self.assertEqual(departures, 2, "Robot should have only one complete tour starting and ending at the depot")
    
    def test_visitation_of_all_cities(self):
        # Test that all cities, except the depot, are visited at least once across all tours:
        # Flatten the list of all tour cities:
        all_cities_visited = sum(self.robot_tours.values(), [])
        
        # Check if each city from 1 to total_cities-1 is visited:
        for city in range(1, self.total_cities):  # city 0 is the depot
            self.assertIn(city, all_cities_visited)

if __name__ == '__main__':
    unittest.main()