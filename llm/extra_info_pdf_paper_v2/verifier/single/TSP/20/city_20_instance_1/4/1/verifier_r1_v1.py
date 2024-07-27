import unittest
from math import sqrt

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        # Given cities (including the depot city at index 0)
        self.cities = [(14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
                       (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
                       (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
                       (50, 28), (69, 9)]

        # Total number of cities
        self.n_cities = 20
        
        # Expected tour and its cost
        self.expected_tour = [0, 14, 3, 5, 7, 4, 16, 10, 11, 17, 19, 18, 15, 8, 1, 13, 12, 9, 2, 6, 0]
        self.expected_cost = 392.4509758542063

    def euclidean_distance(self, p1, p2):
        return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def test_robot_tour(self):
        # Check the number of cities
        self.assertEqual(len(self.cities), self.n_cities, "Number of cities mismatch")
        
        # Check depot city coordinates
        self.assertEqual(self.cities[0], (14, 77), "Depot city coordinates mismatch")
        
        # Check if tour starts and ends at the depot city
        self.assertTrue(self.expected_tour[0] == self.expected_tour[-1] == 0, "Tour does not start or end at the depot city")
        
        # Check if each city is visited exactly once
        self.assertEqual(len(set(self.expected_tour[1:-1])), self.n_cities - 1, "Cities not visited exactly once")
        
        # Calculate the total travel cost from the tour
        calculated_cost = sum(self.euclidean_distance(self.cities[self.expected_tour[i]], self.cities[self.expected_tour[i+1]]) 
                               for i in range(len(self.expected_tour) - 1))
        
        # Check if the tour cost matches the expected cost
        self.assertAlmostEqual(calculated  cost, self.expected_cost, places=6, "Tour cost does not match expected cost")

def run_test():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestRobotTour('test_robot_tour'))
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

run_test()