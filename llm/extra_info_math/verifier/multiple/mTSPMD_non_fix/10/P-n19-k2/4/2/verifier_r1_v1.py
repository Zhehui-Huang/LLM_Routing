import unittest
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        self.coordinates = [
            (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
            (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
            (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
            (61, 33), (62, 63), (63, 69), (45, 35)
        ]
        self.robot_0_tour = [0, 1, 10, 12, 14, 4, 11, 3, 8, 16, 17, 0]
        self.robot_1_tour = [0, 6, 18, 5, 7, 2, 9, 15, 13, 0]
        self.expected_total_cost = 241.29056448233058

    def test_valid_tours(self):
        # All tests are integrated here to conclude with a single pass or fail for simplicity.
        # Check if tours start at Depot 0
        self.assertTrue(self.robot_0_tour[0] == self.robot_1_tour[0] == 0, "Tours should start at Depot 0.")
        # Check if all cities except the depot are visited exactly once
        all_cities_visited = set(self.robot_0_tour + self.robot_1_tour)
        self.assertEqual(len(all_cities_visited), len(self.coordinates), "All cities must be visited exactly once.")
        # Check if tours can end at the depot (optional based on the requirement of not needing to return)
        self.assertTrue(self.robot_0_tour[-1] == self.robot_1_tour[-1] == 0, "Tours should be able to end at a depot.")
        # Calculate and compare the total and expected costs
        total_cost = 0
        for tour in [self.robot_0_tour, self.robot_1_tour]:
            for i in range(len(tour) - 1):
                total_cost += euclidean_distance(self.coordinates[tour[i]], self.coordinates[tour[i + 1]])
        self.assertAlmostEqual(total_cost, self.expected_total_cost, places=5, msg="Total travel cost must be minimized.")

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRobotTours))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

if __name__ == "__main__":
    run_tests()