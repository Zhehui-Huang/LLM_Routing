import unittest
from math import sqrt

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
            (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
            (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
        ]
        self.tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
        self.expected_total_cost = 337.84
        self.expected_max_distance = 60.67

    def test_tour_validity(self):
        self.assertEqual(self.tour[0], 0, "Tour should start at the depot city.")
        self.assertEqual(self.tour[-1], 0, "Tour should end at the depot city.")
        self.assertCountEqual(sorted(set(self.tour)), list(range(15)), "Tour should visit each city exactly once except for the depot.")

    def test_travel_cost_and_distances(self):
        total_cost = 0
        max_distance = 0
        for i in range(1, len(self.tour)):
            city1 = self.cities[self.tour[i-1]]
            city2 = self.cities[self.tour[i]]
            distance = euclidean_distance(city1, city2)
            total_cost += distance
            max_distance = max(max_distance, distance)
        
        self.assertAlmostEqual(total_cost, self.expected_total_category_data_argument_cost, places=2)
        self.assertAlmostEqual(max_distance, self.expected_max_distance, places=2)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTSPSolution))
    result = unittest.TextTestRunner().run(suite)
    # Output Correct or Fail based on the test results
    if not result.wasSuccessful():
        print("FAIL")
    else:
        if result.failures or result.errors:
            print("FAIL")
        else:
            print("CORRECT")

run_tests()