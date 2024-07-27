import unittest
from math import sqrt

def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        self.depot = (30, 40)
        self.cities = [
            (30, 40),  # Depot city 0
            (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
            (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
            (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
        ]
        self.robot_tours = [
            {'tour': [0, 0, 0], 'cost': 0.0},
            {'tour': [0, 0, 0], 'cost': 0.0}
        ]
        self.max_cost = 0.0
    
    def test_begin_end_depot(self):
        for robot in self.robot_tours:
            self.assertEqual(robot['tour'][0], 0)
            self.assertEqual(robot['tour'][-1], 0)

    def test_visit_all_cities_once(self):
        visited = set()
        for robot in self.robot_tours:
            for city in robot['tour'][1:-1]:  # skipping depot from check
                visited.add(city)
        self.assertEqual(len(visited), len(self.cities) - 1)  # exclude depot from cities count

    def test_minimize_max_distance(self):
        reported_max_cost = max(robot['cost'] for robot in self.robot_tours)
        self.assertEqual(reported_max, self.max_cost)

    def test_correct_tour_output_structure(self):
        for robot in self.robot_tours:
            self.assertTrue(all(isinstance(city, int) for city in robot['tour']))
            self.assertTrue(isinstance(robot['cost'], float))

    def test_correct_max_cost_output(self):
        calculated_max_cost = max(robot['cost'] for robot in self.robot_tours)
        self.assertEqual(calculated_max_cost, self.max_cost)
    
    def runTest(self):
        self.test_begin_end_depot()
        self.test_visit_all_cities_once()
        self.test_minimal_distance_in_any_route()
        self.test_correct_tour_output_structure()
        self.test_correct_max_cost_output()

# Create test suite
test_suite = unittest.TestSuite()
test_suite.addTest(TestRobotTours())

# Run tests
runner = unittest.TextTestRunner()
result = runner.run(test_suite)
if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")