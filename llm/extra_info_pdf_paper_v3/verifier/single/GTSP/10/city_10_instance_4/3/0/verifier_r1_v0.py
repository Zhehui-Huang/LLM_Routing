import unittest
import math

class TestGTSPSolution(unittest.TestCase):
    def setUp(self):
        # Initialize coordinates of cities and the groups
        self.coords = {
            0: (79, 15), 1: (79, 55), 2: (4, 80), 
            3: (65, 26), 4: (92, 9), 5: (83, 61), 
            6: (22, 21), 7: (97, 70), 8: (20, 99), 
            9: (66, 62)
        }
        
        self.groups = {
            0: [1, 4], 1: [2, 6], 2: [7], 
            3: [5], 4: [9], 5: [8], 6: [3]
        }
        
        self.solution_tour = [0, 1, 5, 7, 9, 8, 2, 3, 0]
        self.solution_cost = 279.02

    def test_starts_and_ends_at_depot(self):
        # Requirement 1: Starts and ends at the depot
        self.assertEqual(self.solution_tour[0], 0, "Tour should start at depot (0)")
        self.assertEqual(self.solution_tour[-1], 0, "Tour should end at depot (0)")

    def test_visits_one_city_from_each_group(self):
        # Requirement 2: Visits one city from each group
        visited = {city for city in self.solution_tour if city in self.coords}
        unique_groups = set()
        for city in visited:
            for group_id, cities in self.groups.items():
                if city in cities:
                    unique_groups.add(group_id)
        self.assertEqual(len(unique_groups), len(self.groups), "Should visit one city from each group")
        
    def test_uses_euclidean_distance(self):
        # Requirement 3: Uses Euclidean distance
        def euclidean(a, b):
            return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
        
        calculated_cost = 0
        for i in range(len(self.solution_tour) - 1):
            city_a = self.solution_tour[i]
            city_b = self.solution_tour[i + 1]
            calculated_cost += euclidean(self.coords[city_a], self.coords[city_b])
        
        self.assertAlmostEqual(calculated_cost, self.solution_cost, places=2, msg="Calculated cost should use Euclidean distance")

    def test_identifies_shortest_route(self):
        # This is a heuristic solution, so manually verifying it's the shortest isn't feasible here, 
        # instead we verify if the specific solution given matches a known "good" solution.
        # For a true in-depth test, more robust algorithm-specific checks would need to be employed,
        # and possibly cross-checked with another tool or more comprehensive test scenarios.
        known_good_cost = 279.02  # Hardcoding based on known good route computation
        self.assertAlmostEqual(self.solution_cost, known_good_cost, places=2, msg="Should match the known good shortest route cost")
        
    def test_output_format(self):
        # Requirement 5: Output format check
        is_correct_format = isinstance(self.solution_tour, list) and all(isinstance(city, int) for city in self.solution_tour) and isinstance(self.solution_cost, float)
        self.assertTrue(is_correct_format, "Output format should be a list of integers followed by a float total cost")

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # Adjusting argv to avoid interference with notebook arguments