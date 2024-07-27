import unittest
import math

class TestKTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (9, 93),
            1: (8, 51),
            2: (74, 99),
            3: (78, 50),
            4: (21, 23),
            5: (88, 59),
            6: (79, 77),
            7: (63, 23),
            8: (19, 76),
            9: (21, 38),
            10: (19, 65),
            11: (11, 40),
            12: (3, 21),
            13: (60, 55),
            14: (4, 39)
        }
        # Provided solution
        self.tour = [0, 1, 10, 8, 0]
        self.reported_total_travel_cost = 90.54

    def test_tour_length(self):
        # Check if tour length is correct
        self.assertEqual(len(self.tour), 4 + 1)  # including the return to the depot

    def test_start_end_depot(self):
        # Check if tour starts and ends at the depot
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_distance_calculation(self):
        # Check if the travel cost is calculated correctly using Euclidean distance
        def compute_distance(city1, city2):
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        total_distance = sum(compute_distance(self.tour[i], self.tour[i+1]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(total_distance, self.reported_total_travel_cost, places=2)

    def test_unique_cities(self):
        # Check if exactly four unique cities were visited (excluding final return to depot)
        unique_cities = set(self.tour[:-1])
        self.assertEqual(len(unique_cities), 4)

# Running the tests
if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestKTSPSolution))
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")