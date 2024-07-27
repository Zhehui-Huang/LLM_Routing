import unittest
import math

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = {
            0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
            5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
            10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
            15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
        }
        self.groups = {
            0: [7, 10, 11, 12],
            1: [3, 8, 13, 16],
            2: [2, 4, 15, 18],
            3: [1, 9, 14, 19],
            4: [5, 6, 17]
        }
        # Tour provided
        self.tour = [0, 16, 17, 4, 7, 14, 0]
        # Calculated total cost
        self.provided_total_cost = 227.99542744635505
    
    def test_tour_validity(self):
        # Check start and end at depot
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
        
        # Check one city from each group
        selected_groups = set()
        for city in self.tour[1:-1]:  # Exclude the depot city 0 at start and end
            for group_id, cities in self.groups.items():
                if city in cities:
                    selected_groups.add(group_id)
                    break
        self.assertEqual(len(selected_groups), 5)
        
    def test_total_cost_calculation(self):
        calculated_cost = 0
        for i in range(1, len(self.tour)):
            city1 = self.tour[i - 1]
            city2 = self.tour[i]
            x1, y1 = self.coordinates[city1]
            x2, y2 = self.coordinates[city2]
            calculated_cost += math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        # Check if the calculated cost is close to the provided total cost
        self.assertAlmostEqual(calculated_cost, self.provided_total_cost, places=5, msg="Cost miscalculated")
        
    def test_if_solution_is_correct(self):
        try:
            self.test_tour_validity()
            self.test_total_cost_calculation()
            print("CORRECT")
        except AssertionError as e:
            print("FAIL")
            print(str(e))

# Running the tests
test_suite = unittest.TestSuite()
test_suite.addTest(TestTourSolution('test_if_solution_is_correct'))
runner = unittest.TextTestRunner()
runner.run(test_suite)