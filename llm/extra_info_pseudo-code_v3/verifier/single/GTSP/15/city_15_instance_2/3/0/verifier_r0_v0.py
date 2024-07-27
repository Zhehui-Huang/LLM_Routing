import math
import unittest

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestTravelingRobot(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (54, 87),
            1: (21, 84),
            2: (69, 84),
            3: (53, 40),
            4: (54, 42),
            5: (36, 30),
            6: (52, 82),
            7: (93, 44),
            8: (21, 78),
            9: (68, 14),
            10: (51, 28),
            11: (44, 79),
            12: (56, 58),
            13: (72, 43),
            14: (6, 99)
        }
        self.city_groups = [
            [8, 12, 14],
            [7, 10, 11],
            [4, 6, 9],
            [1, 3, 13],
            [2, 5]
        ]
        self.solution_tour = [0, 12, 10, 4, 3, 2, 0]
        self.reported_cost = 138.15

    def test_start_and_end_at_depot(self):
        self.assertEqual(self.solution_tour[0], 0, "Tour should start at the depot")
        self.assertEqual(self.solution_tour[-1], 0, "Tour should end at the depot")

    def test_visit_one_city_from_each_group(self):
        visited_groups = set()
        for city in self.solution_tour[1:-1]:  # Exclude the depot city at start/end
            for i, group in enumerate(self.city_group):
                if city in group:
                    visited_groups.add(i)
                    break
        self.assertEqual(len(visited_groups), len(self.city_groups), "Visited each group exactly once")

    def test_calculate_travel_cost(self):
        calculated_cost = 0
        for i in range(len(self.solution_tour) - 1):
            city1, city2 = self.solution_tour[i], self.solution_tour[i + 1]
            calculated_cost += euclidean_distance(self.cities[city1], self.cities[city2])
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=2, msg="Travel cost should match reported cost")

    def test_output_validation(self):
        # Run all tests
        test_result = unittest.TextTestRunner().run(unittest.makeSuite(TestTravelingRobot))
        if all(test_result.wasSuccessful() for test in test_result.testsRun):
            print("CORRECT")
        else:
            print("FAIL")

# Create an instance of the test case and run the defined tests
test_suite = unittest.TestSuite()
test_suite.addTest(TestTravelingRobot('test_start_and_end_at_depot'))
test_suite.addTest(TestTravelingRobot('test_visit_one_city_from_each_group'))
test_suite.addTest(TestTravelingRobot('test_calculate_travel_cost'))

runner = unittest.TextTestRunner()
runner.run(test_suite)