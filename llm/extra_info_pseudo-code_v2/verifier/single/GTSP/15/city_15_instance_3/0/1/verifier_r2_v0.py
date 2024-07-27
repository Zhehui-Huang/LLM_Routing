import unittest
from math import sqrt

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (16, 90),
            1: (43, 99),
            2: (80, 21),
            3: (86, 92),
            4: (54, 93),
            5: (34, 73),
            6: (6, 61),
            7: (86, 69),
            8: (30, 50),
            9: (35, 73),
            10: (42, 64),
            11: (64, 30),
            12: (70, 95),
            13: (29, 64),
            14: (32, 79)
        }
        self.groups = {
            0: [1, 6, 14],
            1: [5, 12, 13],
            2: [7, 10],
            3: [4, 11],
            4: [2, 8],
            5: [3, 9]
        }
        self.tour = [0, 14, 5, 10, 11, 8, 9, 0]
        self.total_cost = 166.758

    def test_start_end_depot(self):
        "Check if tour starts and ends at the depot city 0"
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_one_from_each_group(self):
        "Check if exactly one city from each group is visited"
        visited = set(self.tour[1:-1])  # Exclude the depot 0 at start and end
        correct_groups = all(any(city in group for city in visited) for group in self.groups.values())
        self.assertTrue(correct_groups)

    def test_tour_cost(self):
        "Check if computed tour cost is close enough to the given value"
        def euclidean_distance(p1, p2):
            return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        
        computed_cost = 0
        for i in range(len(self.tour) - 1):
            computed_cost += euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i+1]])
        
        self.assertAlmostEqual(computed_cost, self.total_cost, places=3)

    def test_output_correctness(self):
        "Check that all requirements are satisfied"
        try:
          self.test_start_end_depot()
          self.test_visit_one_from_each_group()
          self.test_tour_cost()
        except AssertionError:
          return "FAIL"
        return "CORRECT"

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestRobotTour('test_output_correctness'))
    test_result = unittest.TextTestRunner().run(test_suite)
    
    print("CORRECT" if len(test_result.errors) == 0 and len(test_result.failures) == 0 else "FAIL")