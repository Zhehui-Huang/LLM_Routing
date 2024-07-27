import unittest
from math import sqrt

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

class TestMTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
            (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
            (43, 67), (58, 48), (58, 27), (37, 69)
        ]
        self.robot_tours = [
            [0, 8, 10, 0],  # Robot 0
            [1, 13, 12, 1],  # Robot 1
            [2, 9, 14, 2],   # Robot 2
            [3, 11, 15, 3],  # Robot 3
            [4, 7, 5, 4],    # Robot 4
            [5, 6, 4, 5],    # Robot 5
            [6, 8, 10, 6],   # Robot 6
            [7, 9, 13, 7],   # Robot 7
        ]

    def test_solution(self):
        all_visited_cities = sum(self.robot_tours, [])
        unique_cities = set(all_visited_cities)

        # Each city must be visited once
        self.assertEqual(len(all_visited_cities), 16 + (len(self.robot_tours) * 2 - 2))
        self.assertEqual(len(unique_cities), 16)

        # Every tour should start and end at its depot
        for idx, tour in enumerate(self.robot_tours):
            self.assertEqual(tour[0], idx)
            self.assertEqual(tour[-1], idx)

        # Compute total travel cost for all robots
        total_cost = 0
        for tour in self.robot_tours:
            cost = sum(euclidean_distance(self.cities[tour[i]],
                                          self.cities[tour[i + 1]]) for i in range(len(tour) - 1))
            total_cost += cost
            self.assertTrue(cost > 0)  # Each individual cost should be positive

        self.assertTrue(total_cost > 0)  # Overall cost should be positive

def run_tests():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestMTSPSolution))
    test_runner = unittest.TextTestRunner()

    result = test_runner.run(test_suite)
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

print(run_tests())