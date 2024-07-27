import unittest
from math import sqrt

# Mock-up of a sample solution
# This is just a placeholder, you should replace it with the actual solution
solution = {
    'tours': [
        [0, 1, 2, 0],
        [0, 3, 4, 0],
        [0, 5, 6, 0],
        [0, 7, 8, 0],
        [0, 9, 10, 0],
        [0, 11, 12, 0],
        [0, 13, 14, 0],
        [0, 15, 0]
    ],
    'costs': [50, 45, 60, 70, 55, 65, 30, 25],
    'overall_cost': 400
}

class TestVRPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
            (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
            (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
        ]
        self.demand = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
        self.robot_capacity = 35
        self.robot_count = 8

    def test_start_and_end_at_depot(self):
        for tour in solution['tours']:
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)
    
    def test_meet_demands(self):
        demands_met = [0] * len(self.demand)
        for tour in solution['tours']:
            for city in tour[1:-1]:  # Exclude the depot city at start and end
                demands_met[city] += self.demand[city]
        self.assertListEqual(demands_met, self.demand)

    def test_capacity_constraints(self):
        for tour in solution['tours']:
            load = sum(self.demand[city] for city in tour[1:-1])
            self.assertLessEqual(load, self.robot_capacity)

    def test_cost_calculation_and_minimization(self):
        def calculate_distance(city1, city2):
            return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
        
        total_calculated_cost = 0
        for idx, tour in enumerate(solution['tours']):
            tour_cost = sum(calculate_distance(self.cities[tour[i]], self.cities[tour[i + 1]]) for i in range(len(tour) - 1))
            self.assertAlmostEqual(tour_cost, solution['costs'][idx], places=1)
            total_calculated_roat += tour_cost
        self.assertAlmostEqual(total_calculated_cost, solution['overall_cost'], places=1)

    def test_tour_structure(self):
        for tour in solution['tours']:
            self.assertEqual(tour[0], 0)
            self.assertTrue(tour[-1], 0)

    def test_robot_count(self):
        self.assertEqual(len(solution['tours']), self.robot_count)

# Running tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestVRPSolution)
test_result = unittest.TextTestRunner().run(suite)

# Check if all tests passed
output_result = "CORRECT" if test_result.wasSuccessful() else "FAIL"
print(output_result)