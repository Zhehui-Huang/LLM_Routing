import unittest
import math

class TestRobotTourSolution(unittest.TestCase):
    
    def test_tour(self):
        cities = {
            0: (90, 3),   # depot
            1: (11, 17),
            2: (7, 27),
            3: (95, 81),
            4: (41, 54),
            5: (31, 35),
            6: (23, 95),
            7: (20, 56),
            8: (49, 29),
            9: (13, 17)
        }
        groups = [
            [3, 6],
            [5, 8],
            [4, 9],
            [1, 7],
            [2]
        ]
        solution_tour = [0, 3, 5, 9, 1, 2, 0]
        reported_cost = 281.60273931778477
        
        # Check if tour starts and ends at depot (city 0)
        self.assertEqual(solution_tour[0], 0)
        self.assertEqual(solution_tour[-1], 0)
        
        # Check if tour visits one city from each group
        found_groups = [0] * len(groups)
        for city in solution_tour[1:-1]:  # exclude the depot city (start and end)
            for i, group in enumerate(groups):
                if city in group:
                    found_groups[i] += 1
        self.assertTrue(all(count == 1 for count in found_groups))
        
        # Calculate and validate the travel cost
        def euclidean_distance(c1, c2):
            return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

        calculated_cost = sum(euclidean_distance(solution_tour[i], solution_tour[i+1]) for i in range(len(solution_tour) - 1))
        
        # Check if the reported total travel cost matches the calculated travel cost
        self.assertAlmostEqual(calculated_cost, reported_cost, places=5, msg="Calculated cost does not match reported cost")
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # Adjust argv to avoid conflict with Jupyter or similar environments