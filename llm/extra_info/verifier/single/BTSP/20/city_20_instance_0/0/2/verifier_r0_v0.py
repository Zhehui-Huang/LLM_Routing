import unittest
import math

class TestRobotTour(unittest.TestCase):
    # Store the cities coordinates
    cities = [
        (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), 
        (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
        (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), 
        (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
    ]

    # Provided solution to check
    provided_tour = [
        0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18,
        15, 11, 9, 12, 7, 14, 16, 0
    ]
    provided_total_cost = 349.1974047195548
    provided_max_distance = 32.38826948140329

    def calculate_euclidean_distance(self, city1, city2):
        x1, y1 = city1
        x2, y2 = city2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def test_cities_visited_exactly_once(self):
        unique_cities = set(self.provided_tour)
        self.assertEqual(len(unique_cities), 20, "Each city should be visited exactly once with unique entry.")

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.provided_tour[0], 0, "Tour should start at depot city 0.")
        self.assertEqual(self.provided_tour[-1], 0, "Tour should end at depot city 0.")
        
    def test_total_and_max_travel_cost(self):
        total_cost = 0
        maximum_distance = 0
        for i in range(len(self.provided_tour) - 1):
            city_a = self.provided_tour[i]
            city_b = self.provided_tour[i + 1]
            distance = self.calculate_euclidean_distance(self.cities[city_a], self.cities[city_b])
            total_cost += distance
            maximum_distance = max(maximum_distance, distance)

        self.assertAlmostEqual(total_cost, self.provided_total_cost, places=5,
                               msg="Total travel cost should match the provided value.")
        self.assertAlmostEqual(maximum_distance, self.provided_max_distance, places=5,
                               msg="Maximum distance between consecutive cities should match the provided value.")

if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)