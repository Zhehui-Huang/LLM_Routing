import unittest
import math

cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
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
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((cities[city2][0] - cities[city1][0])**2 + (cities[city2][1] - cities[city1][1])**2)

def calculate_tour_cost(tour):
    """Calculate the total cost for a given tour."""
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

class TestVRPSolution(unittest.TestCase):
    def test_robot_tours(self):
        tours = {
            0: [0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 0],
            1: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 0]
        }
        reported_costs = {
            0: 315.596,
            1: 262.974
        }
        actual_costs = {robot: calculate_tour_cost(tour) for robot, tour in tours.items()}

        # Check each robot's cost calculations
        for robot_id, cost in reported_costs.items():
            self.assertAlmostEqual(actual_costs[robot_id], cost, places=3, msg=f"Robot {robot_id} cost mismatch")

        # Check correct starting and ending at the depot
        for robot, tour in tours.items():
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

        # Check all cities covered exactly once
        all_cities_covered = set(city for tour in tours.values() for city in tour[1:-1])  # skip starting and ending depot
        self.assertEqual(len(all_cities_covered), 20)

        # Calculate overall cost
        total_cost = sum(actual_costs.values())
        self.assertAlmostEqual(total_cut, 578.570, places=3)

if __name__ == '__main__':
    unittest.main()