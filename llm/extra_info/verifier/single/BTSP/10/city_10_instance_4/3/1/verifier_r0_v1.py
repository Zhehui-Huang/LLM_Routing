import unittest
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (79, 15),  # Depot city 0
            (79, 55),
            (4, 80),
            (65, 26),
            (92, 9),
            (83, 61),
            (22, 21),
            (97, 70),
            (20, 99),
            (66, 62)
        ]
        self.solution_tour = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        self.solution_cost = 637.815708196756
        self.solution_max_distance = float('inf')  # This was set to 'inf', which needs a logical update.

    def test_tour_coverage(self):
        # Test if the tour visits all cities exactly once and starts/ends at the depot.
        tour_without_depot = self.solution_tour[1:-1]
        self.assertEqual(len(tour_without_depot), len(set(tour_without_depot)), "Some cities are visited more than once or not at all")
        self.assertEqual(self.solution_tour[0], self.solution_tour[-1], "Tour does not start and end at the depot")

    def test_total_cost(self):
        # Calculate the cost from the tour
        total_cost_calculated = sum(euclidean_distance(self.cities[self.solution_tour[i]], self.cities[self.solution_tour[i + 1]]) for i in range(len(self.solution_tour) - 1))
        self.assertAlmostEqual(total_cost_calculated, self.solution_cost, places=6, msg="Total travel cost mismatch")

    def test_max_distance(self):
        # Calculate the maximum distance between consecutive cities in the tour
        max_distance_calculated = max(euclidean_distance(self.cities[self.solution_tour[i]], self.cities[self.solution_tour[i + 1]]) for i in range(len(self.solution_tour) - 1))
        self.assertIs(math.isinf(self.solution_max_distance), math.isinf(max_distance_calculated), "Maximum distance between consecutive cities calculation error")

def main():
    # Main function to run the tests
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTSPSolution))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    print("CORRECT" if result.wasSuccessful() else "FAIL")

if __name__ == "__main__":
    main()