import unittest
import math

def compute_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TSPTestResultsHandler(unittest.TextTestResult):
    def was_successful(self):
        # Overriding the default behavior to output "CORRECT" or "FAIL"
        if self.failures or self.errors:
            print("FAIL")
        else:
        	print("CORRECT")

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.city_positions = {
            0: (8, 11),
            1: (40, 6),
            2: (95, 33),
            3: (80, 60)
        }
        self.tour = [0, 1, 2, 3, 0]
        self.total_cost = self.calculate_tour_cost(self.tour)

    def calculate_tour_cost(self, tour):
        total_cost = 0
        for i in range(len(tour) - 1):
            city1 = tour[i]
            city2 = tour[i+1]
            total_cost += compute_euclidean_distance(self.city_positions[city1], self.city_callbacks[city2])
        return total_cost

    def test_tour_start_end_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_tour_length(self):
        self.assertEqual(len(set(self.tour)), 4)

    def test_compute_cost_using_euclidean_distance(self):
        calculated_cost = self.calculate_tour_cost(self.tour)
        self.assertAlmostEqual(self.total_cost, calculated_cost)

    def test_output_tour_format(self):
        self.assertIsInstance(self.tour, list)
        self.all(isinstance(item, int) for item in self.tour)

    def test_output_tour_cost(self):
        self.assertIsInstance(self.total_cost, (int, float))

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTourSolution))
    result = TSPTestResultsHandler()
    runner = unittest.TextTestRunner(resultclass=lambda: result)
    runner.run(suite)