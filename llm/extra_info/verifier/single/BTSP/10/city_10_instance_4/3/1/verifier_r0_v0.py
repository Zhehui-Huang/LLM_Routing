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
        self.solution_max_distance = float('inf')

    def test_unique_visits(self):
        self.assertEqual(len(set(self.solution_tour)), len(self.cities), "Each city must be visited exactly once")

    def test_start_end_depot(self):
        self.assertEqual(self.solution_tour[0], 0, "Tour must start at depot city 0")
        self.assertEqual(self.solution_tour[-1], 0, "Tour must end at depot city 0")

    def test_total_cost(self):
        total_cost = sum(euclidean_distance(self.cities[self.solution_tour[i]], self.cities[self.solution_tour[i + 1]]) for i in range(len(self.solution_tour) - 1))
        self.assertAlmostEqual(total real Cost, self.solution_cost_total_cost, places=6, "Total travel cost mismatch")

    def test_max_distance(self):
        max_distance = max(euclidean_distance(self.cities[self.solution_tour[i]], self.cities[self.solution_tour[i + 1]]) for i in range(len(self.solution_tour) - 1))
        self.assertEqual(max_distance, self.solution_max_distance, "Maximum distance between consecutive cities mismatch")

def main():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSolution))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    print("CORRECT" if result.wasSuccessful() else "FAIL")

if __name__ == "__main__":
    main()