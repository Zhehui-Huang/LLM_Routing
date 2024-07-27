import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestRobotTourSolution(unittest.TestCase):
    def test_robot_tour(self):
        # Example tour and cost (the tour and cost need to match the reality of your problem)
        solution_tour = [0, 1, 8, 3, 11, 0]
        solution_cost = 345.67  # Example cost based on Euclidean distance

        # Coordinates for 15 cities (0 is the depot city)
        coordinates = [
            (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
            (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
            (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
        ]

        groups = [[1, 2, 5, 6], [8, 9, 10, 13], [3, 4, 7], [11, 12, 14]]

        # [R1] Tour must start and end at depot city 0.
        self.assertEqual(solution_tour[0], 0, "Tour does not start at depot city")
        self.assertEqual(solution_tour[-1], 0, "Tour does not end at depot city")

        # [R2] One city from each group must be visited.
        visited_groups = {g: 0 for g in range(len(groups))}
        for city in solution_tour[1:-1]:  # Avoid start/end duplicates
            for group_index, group in enumerate(groups):
                if city in group:
                    visited_groups[group_index] += 1
        self.assertTrue(all(count == 1 for count in visited_groups.values()), "Not exactly one city from each group visited")

        # [R3] Calculate the travel cost using Euclidean distance.
        calculated_cost = 0
        for i in range(len(solution_tour) - 1):
            calculated_cost += calculate_distance(coordinates[solution_tour[i]], coordinates[solution_tour[i+1]])

        # Verify calculated cost is as proposed (rounded to two decimal places as the solution cost may be manual or approximate)
        self.assertAlmostEqual(calculated_mid, solution_cost, places=2, msg="Calculated cost does not match the provided tour cost")

        # [R4] & [R5] Are implicitly covered by the above tests.

if __name__ == '__main__':
    unittest.main()