import unittest
from math import sqrt

# Define the corrected tour data from the results provided
robots_tours = {
    0: [0, 13, 11, 4, 3, 0],
    1: [1, 2, 1],
    2: [2, 5, 7, 9, 6, 8, 10, 12, 15, 18, 20, 17, 21, 19, 16, 14, 0],
    3: [3, 1, 3]
}

# Provided travel costs as per the solution presented
travel_costs = {
    0: 56.88903303255399,
    1: 8.54400374531753,
    2: 189.74463348166304,
    3: 23.259406699226016
}

# City coordinates as per the problem statement
city_coordinates = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

class TestRobotRouting(unittest.TestCase):
    def test_depots(self):
        """Ensure each robot starts and ends at its assigned depot."""
        for robot_id, tour in robots_tours.items():
            self.assertEqual(tour[0], robot_id, f"Robot {robot_id} does not start at its assigned depot (start {tour[0]}).")
            self.assertEqual(tour[-1], robot_id, f"Robot {robot_id} does not finish at its assigned depot (end {tour[-1]}).")

    def test_unique_visits(self):
        """Ensure each city is visited exactly once by exactly one robot."""
        visits = []
        for tour in robots_tours.values():
            visits.extend(tour[1:-1])  # exclude starting and ending depots
        unique_visits = set(visits)
        self.assertEqual(len(visits), len(unique_visits), "Some cities are visited more than once.")

    def test_travel_costs(self):
        """Validate the travel costs for each robot against given results."""
        for robot_id, tour in robots_tours.items():
            total_cost = 0
            for i in range(len(tour) - 1):
                c1, c2 = city_coordinates[tour[i]], city_coordinates[tour[i + 1]]
                total_cost += sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)
            self.assertAlmostEqual(total_cost, travel_costs[robot_id], places=5, msg=f"Cost mismatch for Robot {robot_id}")

if __name__ == "__main__":
    unittest.main()