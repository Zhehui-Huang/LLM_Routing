import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        # Cities coordinates
        self.cities = {
            0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54),
            5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)
        }
        # Proposed tour and total cost
        self.tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        self.proposed_cost = 531.57

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_all_cities_visited_exactly_once(self):
        visited_cities = set(self.tour)
        all_cities = set(range(len(self.cities)))
        self.assertTrue(all(c in visited_cities for c in all_cities))

    def test_travel_costs_calculated_correctly(self):
        def euclidean_distance(city1, city2):
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        total_calculated_cost = 0
        for i in range(len(self.tour) - 1):
            city1 = self.tour[i]
            city2 = self.tour[i + 1]
            total_calculated_cost += euclidean_distance(city1, city2)

        self.assertAlmostEqual(total_calculated_cost, self.proposed_cost, places=2)

    def test_output_format(self):
        self.assertIsInstance(self.tour, list)
        self.assertIsInstance(self.proposed_cost, float)

def run_tsp_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestTSPSolution('test_tour_starts_and_ends_at_depot'))
    suite.addTest(TestTSPSolution('test_all_cities_visited_exactly_once'))
    suite.addTest(TestTSPSolution('test_travel_costs_calculated_correctly'))
    suite.addTest(TestTSPSolution('test_output_format'))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

# Execute tests
test_result = run_tsp_tests()
print(test_result)