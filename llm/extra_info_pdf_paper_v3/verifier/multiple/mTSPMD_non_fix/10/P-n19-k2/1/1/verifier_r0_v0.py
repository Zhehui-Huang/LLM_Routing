import unittest
from math import sqrt

class TestRobotTours(unittest.TestCase):
    
    # Coordinates of the cities
    cities = {
        0: (30, 40),
        1: (37, 52),
        2: (49, 43),
        3: (52, 64),
        4: (31, 62),
        5: (52, 33),
        6: (42, 41),
        7: (52, 41),
        8: (57, 58),
        9: (62, 42),
        10: (42, 57),
        11: (27, 68),
        12: (43, 67),
        13: (58, 27),
        14: (37, 69),
        15: (61, 33),
        16: (62, 63),
        17: (63, 69),
        18: (45, 35)
    }
    
    # Tour solution
    robot_0_tour = [0, 15, 18, 7, 5, 13, 9, 2, 6, 10, 8, 16, 17, 11, 4, 12, 3, 14]
    robot_0_total_cost = 235.16
    overall_total_cost = 235.16
    
    def test_cities_visit_once(self):
        # Each tour should visit all cities collectively exactly once
        visited = set()
        visited.update(self.robot_0_tour)
        expected_cities = set(self.cities.keys())
        self.assertEqual(visited, expected_cities)
    
    def test_correct_start_and_end_points(self):
        # Robot starts from depot 0 and can stop at any city
        self.assertEqual(self.robot_0_tour[0], 0)  # Starts at depot
        self.assertIn(self.robot_0_tour[-1], self.cities.keys())  # Ends at any city
        
    def test_travel_cost_calculation(self):
        # Checking the travel cost for Robot 0
        calculated_cost = 0
        for i in range(len(self.robot_0_tour) - 1):
            x1, y1 = self.cities[self.robot_0_tour[i]]
            x2, y2 = self.cities[self.robot_0_tour[i+1]]
            calculated_cost += sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.assertAlmostEqual(calculated_cost, self.robot_0_total_cost, places=2)
        
    def test_overall_cost(self):
        # Checking the overall total cost
        self.assertEqual(self.robot_0_total_cost, self.overall_total_cost)
        
# Running the test case
suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTests(loader.loadTestsFromTestCase(TestRobotTours))

runner = unittest.TextTestRunner()
result = runner.run(suite)
print("CORRECT" if result.wasSuccessful() else "FAIL")