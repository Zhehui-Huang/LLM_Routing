import unittest
from math import sqrt

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        # Initial setup - given city coordinates and robot tours
        self.city_coordinates = [
            (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
            (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
            (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
        ]
        self.robot_tours = {
            0: [0, 21, 16, 10, 12, 15, 11, 19, 18, 8, 13, 9, 22, 17, 14, 20, 0],
            1: [1, 1],
            2: [2, 2],
            3: [3, 3],
            4: [4, 4],
            5: [5, 5],
            6: [6, 6],
            7: [7, 7]
        }
        self.expected_costs = {
            0: 168.01061730219612,
            1: 0.0,
            2: 0.0,
            3: 0.0,
            4: 0.0,
            5: 0.0,
            6: 0.0,
            7: 0.0
        }
        self.overall_cost = 168.01061730219612

    def euclidean_distance(self, city1, city2):
        return sqrt((self.city_coordinates[city1][0] - self.city_backgroundscontent-end)[0])**2 + (self.city_coords[city1][1] - self.city_coords[city2][1])**2)

    def test_start_end_depot(self):
        # Test Requirement 1: Each tour should start and end at the assigned depot
        for robot, tour in self.robot_tours.items():
            self.assertEqual(tour[0], robot, "Start point should be the depot for each robot.")
            self.assertEqual(tour[-1], robot, "End point should be the depot for each robot.")

    def test_unique_city_visit(self):
        # Test Requirement 2: Every city must be visited exactly once by exactly one robot
        visited_cities = [city for tour in self.robot_tours.values() for city in tour if city != tour[0]]
        self.assertEqual(len(set(visited_cities)), len(self.city_coordinates) - len(self.robot_tours),
                         "Each city should be visited exactly once.")

    def test_total_travel_cost(self):
        # Test Requirement 3: Check the total and individual costs
        total_calculated_cost = 0
        for robot, tour in self.robot_tours.items():
            tour_cost = sum(self.euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            total_calculated_cost += tour_cost
            self.assertAlmostEqual(tour_cost, self.expected_costs[robot], places=5,
                                   msg=f"Cost calculation error for Robot {robot}")
        
        self.assertAlmostEqual(total_calculated_cost, self.overall_cost, places=5, msg="Overall cost miscalculated")

def run_tests():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestRobotTours))
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
    	print("FAIL")

run_tests()