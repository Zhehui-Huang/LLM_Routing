import unittest
import math

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates for the cities
        self.coordinates = [
            (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
            (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
            (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
            (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
        ]
        # Given tour
        self.tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
        self.total_travel_cost = 458.37
        self.max_distance_between_cities = 68.15

    def test_tour_start_and_end_at_depot(self):
        # Check if the tour starts and ends at depot city 0
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_each_city_once(self):
        # Check if each city is visited exactly once except the starting/ending depot
        unique_cities = set(self.tour)
        self.assertEqual(len(unique_cities), 21)  # Including the depot city visited twice
        self.assertEqual(sorted(unique_cities), list(range(20)))  # Check if all cities are visited

    def test_minimize_maximum_distance(self):
        # Calculate the maximum distance between consecutive cities to verify
        def euclidean_distance(p1, p2):
            return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        
        max_dist = max(euclidean_distance(self.coordinates[self.tour[i]], self.coordinates[self.tour[i + 1]]) for i in range(len(self.tour) - 1))
        # We compare computed max_dist with provided max distance within precision errors
        self.assertAlmostEqual(max_dist, self.max_distance_between_cities, places=2)

if __name__ == "__main__":
    unittest.main()