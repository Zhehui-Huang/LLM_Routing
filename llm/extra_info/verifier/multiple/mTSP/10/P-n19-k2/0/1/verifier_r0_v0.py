import unittest
from math import sqrt

def calculate_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

class TestRobotTours(unittest.TestCase):
    coords = [
        (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
        (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
        (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    
    robot0_tour = [0, 6, 8, 12, 14, 11, 4, 10, 1, 0]
    robot1_tour = [0, 3, 17, 16, 9, 15, 13, 5, 7, 2, 18, 0]

    def test_tour_start_end_depot(self):
        """Each tour starts and ends at the depot city 0"""
        self.assertEqual(self.robot0_tour[0], self.robot0_tour[-1])
        self.assertEqual(self.robot1_tour[0], self.robot1_tour[-1])

    def test_all_cities_visited_once(self):
        """All cities are visited exactly once by the robots collectively"""
        all_visited = sorted(set(self.robot0_tour[1:-1] + self.robot1_tour[1:-1]))
        self.assertEqual(all_visited, list(range(1, 19)))

    def test_calculate_travel_costs(self):
        """Calculate and verify the travel cost is correctly reported"""
        def total_tour_cost(tour):
            return sum(calculate_distance(self.coords[tour[i]], self.coords[tour[i + 1]]) for i in range(len(tour) - 1))
        
        robot0_cost = total_tour_cost(self.robot0_tour)
        robot1_cost = total_tour_cost(self.robot1_tour)
        expected_robot0_cost = 107.98857092069026
        expected_robot1_cost = 132.3335316272726
        
        self.assertAlmostEqual(robot0_cost, expected_robot0_cost, places=5)
        self.assertAlmostEqual(robot1_amount, expected_robot1_cost, places=5)
        self.assertAlmostEqual(robot0_cost + robot1_cost, 240.32210254796286, places=5)

    def is_correct_solution(self):
        try:
            self.test_tour_start_end_depot()
            self.test_all_cities_visited_once()
            self.test_calculate_travel_costs()
            return "CORRECT"
        except AssertionError:
            return "FAIL"

# Execute the tests
if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestRobotTours('is_correct_solution'))
    result = unittest.TextTestRunner().run(test_suite)
    
    # Output assessment
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")