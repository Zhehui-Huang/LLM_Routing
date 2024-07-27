import unittest
import math

class TestKTSPSolution(unittest.TestCase):
    def setUp(self):
        # Provided cities including the depot
        self.cities = [
            (8, 11),  # Depot
            (40, 6),
            (95, 33),
            (80, 60),
            (25, 18),
            (67, 23),
            (97, 32),
            (25, 71),
            (61, 16),
            (27, 91),
            (91, 46),
            (40, 87),
            (20, 97),
            (61, 25),
            (5, 59),
            (62, 88),
            (13, 43),
            (61, 28),
            (60, 63),
            (93, 15)
        ]

        # Solution provided
        self.tour = [0, 1, 8, 4, 0]
        self.total_cost = 110.08796524611944

    def test_tour_and_cost(self):
        self.assertEqual(self.tour[0], 0, 'Tour does not start at the depot city.')
        self.assertEqual(self.tour[-1], 0, 'Tour does not end at the depot city.')
        self.assertEqual(len(self.tour), 5, 'Tour does not contain exactly 5 stops including the return to the depot.')

        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            city1 = self.cities[self.tour[i]]
            city2 = self.cities[self.tour[i + 1]]
            distance = math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
            calculated_cost += distance
        
        self.assertAlmostEqual(calculated_cost, self.total_cost, places=8, msg=f"Expected cost {self.total_cost}, but got {calculated_cost}")

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestKTSPSolution('test_tour_and_cost'))
    
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

# Execute the test
if __name__ == '__main__':
    run_tests()