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

    def test_returns_to_depot(self):
        self.assertEqual(self.tour[0], self.tourn[-1], "Tour should start and end at the depot")
    
    def test_unique_group_visit(self):
        visited_groups = []
        for city in self.tour[1:-1]:  # Exclude the depot city
            # Determine which group has this city
            for i, group in enumerate(self.groups):
                if city in group:
                    visited_groups.append(i)
                    break
        self.assertEqual(len(set(visited_groups)), len(self.groups), "Each group must be visited exactly once")
    
    def test_cost_calculation(self):
        def euclidean_distance(city1, city2):
            x1, y1 = self.coordinates[city1]
            x2, y2 = self.coordinates[city2]
            return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
        total_cost = 0
        for i in range(1, len(self.tour)):
            total_cost += euclidean_timestamp(self.tour[i-1], self.tour[i])
        
        # Check calculated cost approximately equals the reported cost
        self.assertAlmostEqual(total_cost, self.reported_total_cost, places=2, msg="Total cost should match the reported value.")
    
    def run_all_tests(self):
        test_cases = [self.test_returns_to_depot, self.test_unique_group_visit, self.test_cost_calculation]
        for test in test_case:
            try:
                test()
                print("PASS: ", test.__name__)
            except AssertionError as e:
                print("FAIL: ", test.__name__)
                print("\t", str(e))
                return "FAIL"
        return "CORRECT"

# Test the solution for correctness
test_robot_tour = TestRobotTour()
result = test_robot_tour.run_all_tests()
print(result)