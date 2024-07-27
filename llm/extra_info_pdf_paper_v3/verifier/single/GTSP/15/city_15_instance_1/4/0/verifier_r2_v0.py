import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestRobotTourSolution(unittest.TestCase):
    def test_robot_tour(self):
        # Example of a hypothetical solution format
        solution_tour = [0, 1, 8, 3, 11, 0]
        solution_cost = 345.67

        # Coordinates for 15 cities (0 is the depot city)
        coordinates = [
            (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
            (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
            (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
        ]

        groups = [[1, 2, 5, 6], [8, 9, 10, 13], [3, 4, 7], [11, 12, 14]]

        # [Requirement 1] Check start and end at depot city 0
        self.assertEqual(solution_tour[0], 0, "Tour does not start at depot city 0")
        self.assertEqual(solution_tour[-1], 0, "Tour does not end at depot city 0")

        # [Requirement 2] One city from each group
        selected_from_groups = set()
        for city in solution_tour:
            for i, group in enumerate(groups):
                if city in group:
                    selected_from_groups.add(i)
        self.assertSetEqual(selected_from_groups, set(range(len(groups))), "Not exactly one city from each group visited")

        # [Requirement 3] Verify the tour's cost calculation
        calculated_cost = 0
        last_city_index = solution_tour[0]
        for city_index in solution_tour[1:]:
            calculated_cost += calculate_distance(coordinates[last_city_index], coordinates[city_index])
            last_city_index = city_index
        self.assertAlmostEqual(calculated_cost, solution_cost, places=2, msg="Calculated cost does not match the provided tour cost")

        # [Requirement 4] Tour starts and ends at city 0
        self.assertEqual(solution_tour[0], 0, "Tour does not start at city 0")
        self.assertEqual(solution_tour[-1], 0, "Tour does not end at city 0")

        # [Requirement 5] Ensure cost is provided
        self.assertIsInstance(solution_cost, (float, int), "Total travel cost is not provided or in incorrect format")

if __name__ == '__main__':
    unittest.main()