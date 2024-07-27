import unittest
import math

# Mock input data and variables (used directly in the test code)
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

tours = {
    0: [0, 0],
    1: [1, 10, 1],
    2: [2, 13, 2],
    3: [3, 8, 12, 3],
    4: [4, 11, 15, 4],
    5: [5, 14, 5],
    6: [6, 6],
    7: [7, 9, 7]
}

costs = {
    0: 0.0,
    1: 14.142135623730951,
    2: 18.110770276274835,
    3: 33.94039963350503,
    4: 26.480522629341756,
    5: 16.97056274847714,
    6: 0.0,
    7: 20.09975124224178
}

total_cost_reported = 129.7441421535715

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_total_cost(tours):
    total_cost = 0
    for robot_id, tour in tours.items():
        tour_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        total_cost += tour_cost
    return total_cost

class TestVRPSolution(unittest.TestCase):
    def test_robot_return_to_depot(self):
        for robot_id, tour in tours.items():
            self.assertEqual(tour[0], tour[-1], f"Robot {robot_id} does not start and end at the same depot.")

    def test_all_cities_visited_once(self):
        all_cities = sum(tours.values(), [])
        unique_cities = set(all_cities)
        self.assertEqual(len(cities), len(unique_cities), "Not all cities are visited exactly once or some are visited more than once.")

    def test_travel_cost_calculations(self):
        for robot_id, tour in tours.items():
            calculated_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
            self.assertAlmostEqual(calculated_cost, costs[robot_id], places=5, msg=f"Calculated cost does not match reported cost for Robot {robot_id}.")

    def test_total_cost(self):
        calculated_total_cost = calculate_total_cost(tours)
        self.assertAlmostEqual(calculated_total_cost, total_cost_reported, places=5, msg=f"Total cost does not match reported total cost.")

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestVRPSolution))
    test_results = unittest.TextTestRunner().run(test_suite)
    print("CORRECT" if test_results.wasSuccessful() else "FAIL")