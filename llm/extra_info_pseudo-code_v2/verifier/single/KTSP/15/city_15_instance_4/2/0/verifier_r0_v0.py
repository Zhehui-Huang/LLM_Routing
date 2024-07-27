import math
import unittest

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = {
            0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
            5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
            10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
        }
        self.tour = [0, 5, 9, 7, 2, 10, 13, 8, 3, 6, 11, 12, 0]
        self.reported_cost = 332.24

    def test_tour_length(self):
        # Check if the tour visits exactly 12 cities including the depot
        self.assertEqual(len(set(self.tour)), 12)

    def test_tour_starts_and_ends_at_depot(self):
        # Check if the tour starts and ends at the depot city 0
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_tour_cost(self):
        # Calculate the travel cost and compare with the reported cost
        def euclidean_distance(c1, c2):
            return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)
        
        actual_cost = 0
        for i in range(len(self.tour)-1):
            city1 = self.tour[i]
            city2 = self.tour[i+1]
            actual_cost += euclidean_distance(self.coordinates[city1], self.coordinates[city2])
        
        self.assertAlmostEqual(actual_cost, self.reported_cost, places=2)

    def test_correct_cities(self):
        # Ensure all cities' coordinates correspond to specified values
        for idx, coord in self.coordinates.items():
            if idx == 0:
                self.assertEqual(coord, (35, 40))  # Depot coordinates
            else:
                self.assertIn(coord, self.coordinates.values())  # Check if the coordinates are within specified

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTSPSolution))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if result.wasSuccessful() and not result.failures and not result.errors:
        return "CORRECT"
    else:
        return "FAIL"

# Run tests and print if the solution is CORRECT or FAIL
print(run_tests())