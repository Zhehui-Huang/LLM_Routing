import unittest
import math

class TestKTSPSolution(unittest.TestCase):
    def setUp(self):
        # Given city coordinates with city 0 being the depot
        self.cities = {
            0: (8, 11),
            1: (40, 6),
            8: (61, 16),
            4: (25, 18)
        }
        # Solution tour and cost provided
        self.tour = [0, 1, 8, 4, 0]
        self.reported_total_cost = 110.08796524611944

    def test_tour_start_end_at_depot(self):
        self.assertEqual(self.tour[0], 0)  # Start at depot
        self.assertEqual(self.tour[-1], 0)  # End at depot

    def test_tour_length(self):
        self.assertEqual(len(set(self.tour)), 4)  # Includes depot, so 3 other cities + depot

    def test_cost_calculation(self):
        def euclidean_dist(city1, city2):
            x1, y1 = city1
            x2, y2 = city2
            return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            calculated_cost += euclidean_dist(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
        
        self.assertAlmostEqual(calculated_cost, self.reported_total_cost, places=5)

# Run tests and capture results
suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTests(loader.loadTestsFromTestCase(TestKTSPSolution))

runner = unittest.TextTestRunner()
result = runner.run(suite)

# Check if the tests succeeded
if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")