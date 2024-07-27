import unittest
import math

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.coordinates = {
            0: (84, 67),
            1: (74, 40),
            2: (71, 13),
            3: (74, 82),
            4: (97, 28),
            5: (0, 31),
            6: (8, 62),
            7: (74, 56),
            8: (85, 71),
            9: (6, 76)
        }
        self.groups = [
            [7, 9],
            [1, 3],
            [4, 6],
            [8],
            [5],
            [2]
        ]
        self.tour = [0, 7, 1, 4, 8, 5, 2, 0]
        self.reported_total_cost = 324.18
    
    def euclidean_distance(self, city1, city2):
        x1, y1 = self.coordinates[city1]
        x2, y2 = self.coordinates[city2]
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    def test_returns_to_depot(self):
        self.assertEqual(self.tour[0], self.tour[-1], "Tour should start and end at the depot")
    
    def test_unique_group_visit(self):
        visited = {g: False for g in range(len(self.groups))}
        for city in self.tour[1:-1]:  # Exclude the start and end (depot)
            for i, group in enumerate(self.groups):
                if city in group:
                    self.assertFalse(visited[i], f"Group {i} visited more than once.")
                    visited[i] = True
        self.assertTrue(all(visited.values()), "Not all groups were visited.")
    
    def test_cost_calculation(self):
        total_cost = 0
        for i in range(1, len(self.tour)):
            total_cost += self.euclidean_distance(self.tour[i-1], self.tour[i])
        
        self.assertAlmostEqual(total_cost, self.reported_total_cost, places=2, msg="Total cost should match the reported value.")
        
if __name__ == '__main__':
    unittest.main()