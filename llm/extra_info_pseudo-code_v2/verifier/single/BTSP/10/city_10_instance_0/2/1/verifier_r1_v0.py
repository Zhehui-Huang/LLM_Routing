import unittest
import math

class TestTravelingRobotSolution(unittest.TestCase):
    def test_solution(self):
        # Coordinates for each city, indexed from 0 to 9
        coordinates = [
            (50, 42),  # Depot city 0
            (41, 1),   # City 1
            (18, 46),  # City 2
            (40, 98),  # City 3
            (51, 69),  # City 4
            (47, 39),  # City 5
            (62, 26),  # City 6
            (79, 31),  # City 7
            (61, 90),  # City 8
            (42, 49)   # City 9
        ]

        # Provided solution details
        tour = [0, 1, 5, 2, 4, 3, 8, 9, 6, 7, 0]
        claimed_total_cost = 328.3966856465968
        claimed_max_distance = 45.18849411078001

        # Requirement 1: Check if each city is visited exactly once and starts/ends at the depot
        self.assertEqual(tour[0], 0)                  # Starts at depot
        self.assertEqual(tour[-1], 0)                 # Ends at depot
        self.assertCountEqual(tour[1:-1], range(1, 10))  # Each city exactly once

        # Requirement 3: Compute the actual tour costs and the max distance between consecutive cities
        actual_cost = 0
        actual_max_distance = 0
        for i in range(len(tour) - 1):
            city1 = coordinates[tour[i]]
            city2 = coordinates[tour[i + 1]]
            distance = math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)
            actual_cost += distance
            actual_max_distance = max(actual_max_distance, distance)

        # Check if the total travel cost and the maximum distance are as claimed
        self.assertAlmostEqual(actual_cost, claimed_total_cost, places=5)
        self.assertAlmostEqual(actual_max_distance, claimed_max_distance, places=5)

# Running the unit test
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)