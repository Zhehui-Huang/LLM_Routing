import unittest
from math import sqrt

# Coordinates for all cities including the depot
cities_coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), 
    (72, 90), (54, 46), (8, 70), (97, 62), 
    (14, 41), (70, 44), (27, 47), (41, 74),
    (53, 80), (21, 21), (12, 39)
]

def euclidean_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
        self.claimed_total_cost = 337.8447016788252
        self.claimed_max_distance = 60.67124524847005

    def test_tour_start_end_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_tour_visits_all_cities_exactly_once(self):
        unique_cities = set(self.tour)
        expected_cities = set(range(15))
        self.assertEqual(unique_cities, expected_cities)

    def test_total_travel_cost(self):
        calculated_cost = sum(euclidean_distance(self.tour[i], self.tour[i+1]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(calculated_cost, self.claimed_total_cost, places=5)

    def test_maximum_distance_between_consecutive_cities(self):
        max_distance = max(euclidean_distance(self.tour[i], self.tour[i+1]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(max_distance, self.claimed_max_distance, places=5)

# Run the tests
if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestTSPSolution))
    result = unittest.TextTestRunner(verbosity=2).run(test_suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")