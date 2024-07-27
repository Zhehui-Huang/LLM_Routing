import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates of the cities
        self.cities = {
            0: (79, 15),
            1: (79, 55),
            2: (4, 80),
            3: (65, 26),
            4: (92, 9),
            5: (83, 61),
            6: (22, 21),
            7: (97, 70),
            8: (20, 99),
            9: (66, 62)
        }
        # Provided solution tour
        self.tour = [0, 1, 3, 4, 5, 7, 9, 8, 2, 6, 0]
        # Provided total cost and maximum distance
        self.provided_total_travel_cost = 637.815708196756
        self.provided_max_distance = 61.68468205316454
    
    def euclidean_distance(self, city1, city2):
        x1, y1 = self.cities[city1]
        x2, y2 = self.cities[city2]
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def test_starts_and_ends_at_depot(self):
        # The tour should start and end at the depot city (index 0)
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visits_each_city_once(self):
        # Each city should be visited exactly once except the starting/ending city
        visited_cities = self.tour[1:-1]  # exclude starting/ending depot city occurences
        unique_cities = set(visited_cities)
        self.assertEqual(len(unique_cities), 9)  # check for 9 unique cities

    def test_euclidean_distance_calculation(self):
        # Calculate total distance using the provided tour and check with provided values
        total_cost_calculated = sum(self.euclidean_distance(self.tour[i], self.tour[i+1]) for i in range(len(self.tour)-1))
        max_distance_calculated = max(self.euclidean_distance(self.tour[i], self.tour[i+1]) for i in range(len(self.tour)-1))
        
        # Assert total cost and max distances as closer to the provided within reasonable precision
        self.assertAlmostEqual(total_cost_calculated, self.provided_total_travel_cost, places=2)
        self.assertAlmostEqual(max_distance_calculated, self.provided_max_distance, places=2)

if __name__ == "__main__":
    unittest.main()