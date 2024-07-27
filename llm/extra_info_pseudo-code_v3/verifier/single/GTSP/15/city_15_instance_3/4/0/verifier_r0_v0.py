import unittest
import math

class TestTSPSolution(unittest.TestCase):

    def test_solution(self):
        # Provided tour and cost
        tour = [0, 14, 5, 10, 11, 8, 9, 0]
        reported_cost = 166.76

        # City coordinates
        coordinates = {
            0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 5: (34, 73),
            6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73), 10: (42, 64), 11: (64, 30),
            12: (70, 95), 13: (29, 64), 14: (32, 79)
        }

        # City groups
        groups = {
            0: [1, 6, 14],
            1: [5, 12, 13],
            2: [7, 10],
            3: [4, 11],
            4: [2, 8],
            5: [3, 9]
        }
        
        # Check if tour starts and ends at the depot 0
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)
        
        # Check if one city from each group is visited
        visited_groups = set()
        for city in tour:
            for group_id, cities in groups.items():
                if city in cities:
                    visited_groups.add(group_id)
        self.assertEqual(len(visited_groups), len(groups))

        # Calculate and confirm the total distance
        def euclidean_dist(c1, c2):
            return math.sqrt((coordinates[c1][0] - coordinates[c2][0])**2 + 
                             (coordinates[c1][1] - coordinates[c2][1])**2)

        total_distance = 0
        for i in range(len(tour) - 1):
            total_distance += euclideanDist(tour[i], tour[i + 1])
            
        # Check calculated distance is close to reported within a tolerance
        self.assertAlmostEqual(total_distance, reported_cost, places=2)
        
        # If all checks pass, print that solution is correct
        print("CORRECT")

# Run the test case
test_suite = unittest.TestSuite()
test_suite.addTest(TestTSPSolution('test_solution'))
runner = unittest.TextTestRunner()
runner.run(test_suite)