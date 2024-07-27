import unittest
from math import sqrt

# Define the input data as presented in the provided solution
robots_tours = {
    0: [0, 13, 11, 4, 3, 0],
    1: [1, 2, 1],
    2: [2, 5, 7, 9, 6, 8, 10, 12, 15, 18, 20, 17, 21, 19, 16, 14, 0, 2],
    3: [3, 1, 3]
}

travel_costs = {
    0: 56.88903303255399,
    1: 8.54400374531753,
    2: 189.74463348166304,
    3: 23.259406699226016
}

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
            self.assertEqual(tour[0], robot_id, f"Robot {robot_id} does not start at its assigned depot.")
            self.assertEqual(tour[-1], robot_id, f"Robot {robot_id} does not end at its assigned depot.")

    def test_unique_visits(self):
        """Ensure each city is visited exactly once."""
        visits = sum((tour[1:-1] for tour in robots_tours.values()), [])
        unique_visits = set(visits)
        self.assertEqual(len(visits), len(unique_visits), "Some cities are visited more than once.")

    def test_travel_costs(self):
        """Validate calculated travel costs for consistency with recorded costs."""
        for robot_id, tour in robots_tours.items():
            computed_cost = sum(sqrt((city_coordinates[tour[i]][0] - city_coordinates[tour[i+1]][0]) ** 2 +
                                     (city_coordinates[tour[i]][1] - city_coordinates[tour[i+1]][1]) ** 2)
                                for i in range(len(tour) - 1))
            self.assertAlmostEqual(computed_cost, travel_costs[robot_id], places=5,
                                   msg=f"Cost mismatch for Robot {robot_id}")

if __name__ == "__main__":
    unittest.main()