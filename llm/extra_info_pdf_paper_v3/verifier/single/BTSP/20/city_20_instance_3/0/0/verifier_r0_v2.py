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
        self.tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 
                     12, 8, 14, 0]
        self.total_travel_cost = 458.37
        self.max_distance_between_cities = 68.15

    def test_tour_start_and_end_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_each_city_once(self):
        unique_cities = set(self.tour)
        expected_cities = set(range(20))
        depot_count = self.tour.count(0)
        self.assertEqual(depot_count, 2)
        self.assertEqual(unique_cities, expected_cities)

    def test_minimize_maximum_distance(self):
        def euclidean_distance(p1, p2):
            return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        max_dist = max(euclidean_distance(self.coordinates[self.tour[i]], 
                                          self.coordinates[self.tour[i + 1]]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(max_dist, self.max_distance_between_cities, places=2)

def run_tests():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestTourSolution))
    
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

if __name__ == "__main__":
    run_tests()