import unittest
import math

class TestGTSPSolution(unittest.TestCase):

    def setUp(self):
        self.cities = {
            0: (8, 11),
            1: (40, 6),
            2: (95, 33),
            3: (80, 60),
            4: (25, 18),
            5: (67, 23),
            6: (97, 32),
            7: (25, 71),
            8: (61, 16),
            9: (27, 91),
            10: (91, 46),
            11: (40, 87),
            12: (20, 97),
            13: (61, 25),
            14: (5, 59),
            15: (62, 88),
            16: (13, 43),
            17: (61, 28),
            18: (60, 63),
            19: (93, 15)
        }
        self.groups = {
            0: [1, 3, 5, 11, 13, 14, 19],
            1: [2, 6, 7, 8, 12, 15],
            2: [4, 9, 10, 16, 17, 18]
        }
        self.proposed_solution = [0, 1, 8, 4, 0]
        self.proposed_cost = 110.09

    def test_all_requirements_met(self):
        # Check if the tour starts and ends at the depot.
        self.assertEqual(self.proposed_solution[0], 0, "Tour should start at the depot")
        self.assertEqual(self.proposed_solution[-1], 0, "Tour should end at the depot")
        
        # Check if exactly one city from each group is visited.
        visited_groups = set()
        for city in self.proposed_solution:
            for group_index, group_cities in self.groups.items():
                if city in group_cities:
                    visited_groups.add(group_index)
        self.assertEqual(len(visited_groups), 3, "Should visit one city from each group")
        
        # Calculate the total travel distance.
        total_distance = 0
        for i in range(len(self.proposed_solution) - 1):
            x1, y1 = self.cities[self.proposed_solution[i]]
            x2, y2 = self.cities[self.proposed_solution[i + 1]]
            total_distance += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        # Check if the calculated distance matches the proposed cost.
        self.assertAlmostEqual(total_distance, self.proposed_cost, places=2, "Total distance does not match the proposed cost")

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestGTSPSolution("test_all_requirements_met"))
    
    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

output = run_tests()
print(output)