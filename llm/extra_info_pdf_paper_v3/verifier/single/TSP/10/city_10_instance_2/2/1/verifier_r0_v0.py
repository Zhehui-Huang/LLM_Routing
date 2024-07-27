import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (90, 3),   # Depot city 0
            (11, 17),  # City 1
            (7, 27),   # City 2
            (95, 81),  # City 3
            (41, 54),  # City 4
            (31, 35),  # City 5
            (23, 95),  # City 6
            (20, 56),  # City 7
            (49, 29),  # City 8
            (13, 17)   # City 9
        ]
        self.tour = [0, 8, 5, 4, 7, 6, 3, 2, 1, 9, 0]
        self.reported_cost = 416.8322265347456

    def test_starts_at_depot(self):
        self.assertEqual(self.tour[0], 0, "The tour should start at depot city 0")

    def test_ends_at_depot(self):
        self.assertEqual(self.tour[-1], 0, "The tour should end at depot city 0")

    def test_visits_each_city_once(self):
        unique_cities = set(self.tour[1:-1])  # Exclude the duplicate start/end city
        self.assertEqual(len(unique_cities), 9, "Should visit each of the 9 cities only once")

    def test_total_travel_cost(self):
        total_cost = 0
        for i in range(len(self.tour) - 1):
            total_cost += calculate_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
        self.assertAlmostEqual(self.reported_cost, total_cost, places=5, msg="The reported total travel cost should match the calculated cost")

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

# Execute the tests
print(run_tests())