import unittest
from math import sqrt

def euclidean_distance(city_a, city_b):
    return sqrt((city_a[0] - city_city_b[0])**2 + (city_a[1] - city_b[1])**2)

class TestRobotTourSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
            5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
            10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
        }
        self.groups = [
            [1, 2, 5, 6], [8, 9, 10, 13], [3, 4, 7], [11, 12, 14]
        ]
        self.tour = [0, 5, 10, 4, 11, 0]
        self.reported_cost = 184.24

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour does not start at depot")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at depot")

    def test_visit_one_city_from_each_group(self):
        visited = set(self.tour[1:-1])  # exclude the depot
        self.assertTrue(all(any(city in visited for city in group) for group in self.groups),
                        "Not exactly one city from each group is visited")

    def test_correct_travel_cost(self):
        total_cost = sum(
            euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
            for i in range(len(self.tour) - 1)
        )
        self.assertAlmostEqual(total_cost, self.reported_cost, places=2, msg="Reported travel cost is incorrect")

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestRobotTourSolution('test_tour_starts_and_ends_at_depot'))
    suite.addTest(TestRobotTourSolution('test_visit_one_city_from_each_group'))
    suite.addTest(TestRobotTourSolution('test_correct_travel_cost'))

    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

print(run_tests())