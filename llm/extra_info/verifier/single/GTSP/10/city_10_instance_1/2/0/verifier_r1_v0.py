import unittest
import math

# Coordinates with depot city 0 at the first position
coordinates = [
    (53, 68),  # Depot 0
    (75, 11),  # City 1
    (95, 89),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

# Grouping of cities
city_groups = [
    [5, 6, 7],  # Group 0
    [2, 3],     # Group 1
    [1, 9],     # Group 2
    [4, 8]      # Group 3
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

class TestTSPVRPSolution(unittest.TestCase):
    def test_tour(self):
        tour = [0, 5, 2, 9, 8, 0]
        expected_cost = 183.98559431675523
        
        # Check if the tour starts and ends at the depot
        self.assertEqual(tour[0], 0, "Tour does not start at the depot")
        self.assertEqual(tour[-1], 0, "Tour does not end at the depot")
        
        # Check if exactly one city from each group is visited
        visited = set(tour[1:-1])  # Ignore the depot at start and end
        self.assertTrue(all(len(visited.intersection(group)) == 1 for group in city_groups), "Not exactly one city from each group is visited")
        
        # Calculate the travel cost and check it
        total_cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
        self.assertAlmostEqual(total_cost, expected_cost, places=5, msg="Calculated cost does not match expected cost")
        
        print("CORRECT" if self._outcome.success else "FAIL")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)