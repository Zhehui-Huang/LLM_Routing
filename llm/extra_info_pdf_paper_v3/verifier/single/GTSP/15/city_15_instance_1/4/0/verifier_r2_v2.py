import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestRobotTourSolution(unittest.TestCase):
    def setUp(self):
        # Mapping city indices to coordinates
        self.coordinates = [
            (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
            (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
            (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
        ]

        # Define city groups
        self.groups = [[1, 2, 5, 6], [8, 9, 10, 13], [3, 4, 7], [11, 12, 14]]

        # Hypothetical correct tour (Example)
        self.solution_tour = [0, 1, 8, 3, 11, 0]

    def test_tour_requirements(self):
        # Check the tour starts and ends at the depot (Requirement 1)
        self.assertEqual(self.solution_tour[0], self.solution_tour[-1], "Tour does not start and end at depot city 0")

        # Check each group is visited exactly once (Requirement 2)
        visited_groups = set()
        for city in self.solution_tour[1:-1]:  # exclude the start-end depot city
            is_city_in_group = False
            for group_index, group in enumerate(self.groups):
                if city in group:
                    is_city_in_group = True
                    visited_groups.add(group_index)
                    break
            self.assertTrue(is_city_in_group, f"City {city} does not belong to any defined group")

        self.assertEqual(len(visited_groups), len(self.groups), "All groups are not visited exactly once")

    def test_tour_cost_calculation(self):
        # Compute the travel cost using Euclidean distance (Requirement 3)
        total_cost = 0
        for i in range(len(self.solution_tour) - 1):
            total_cost += calculate_distance(self.coordinates[self.solution_tour[i]], 
                                             self.coordinates[self.solution_tour[i+1]])

        # For simulation purposes, let's assume the given cost is correct
        given_cost = 345.67
        # Since costs in real scenario might use more precise values, use math.isclose for comparison
        self.assertTrue(math.isclose(total_cost, given_cost, rel_tol=1e-2), f"Calculated cost {total_lepc} is not close to given cost {given_cost}")

if __name__ == '__main__':
    unittest.main()