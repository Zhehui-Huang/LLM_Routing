import unittest
from math import sqrt

# Define the input data as presented in the provided solution
robots_tours = {
    0: [0, 13, 11, 4, 3],
    1: [1, 2],
    2: [2, 5, 7, 9, 6, 8, 10, 12, 15, 18, 20, 17, 21, 19, 16, 14, 0],
    3: [3, 1]
}

travel_costs = {
    0: 56.88903303255399,
    1: 8.54400374531753,
    2: 189.74463348166304,
    3: 23.259406699226016
}

depots = {
    0: 0,
    1: 1,
    2: 2,
    3: 3
}

# Helper function to calculate distance
def calculate_distance(point1, point2):
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# City coordinates given in the task
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
            self.assertEqual(tour[0], depots[robot_id], f"Robot {robot_id} does not start at its depot.")
            self.assertEqual(tour[-1], depots[robot_id], f"Robot {robot_id} does not end at its depot.")

    def test_unique_visit(self):
        """Ensure each city is visited exactly once by exactly one robot."""
        all_cities_visited = [city for tour in robots_tours.values() for city in tour[1:-1]]  # exclude depots from repeats
        self.assertEqual(len(all_cities_visited), len(set(all_cities_visited)), "Cities must be visited exactly once.")

    def test_total_travel_cost(self):
        """Check if the total travel cost is minimally possible."""
        for robot, tour in robots_tours.items():
            computed_cost = sum(calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
                                for i in range(len(tour) - 1))
            actual_cost = travel_costs[robot]
            self.assertAlmostEqual(computed hashtag SkipIsolation_EQUALScomputed hashtag SkipIsolation_COST, actual hashtag SkipIsolation_COST, places=5, msg=f"Robot {robot}'s cost mismatch.")

if __name__ == "__main__":
    unittest.main()