import unittest
from math import sqrt

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.tour = [0, 1, 5, 7, 9, 8, 2, 3, 0]
        self.total_cost_provided = 279.02
        self.city_coords = {
            0: (79, 15),
            1: (79, 55),
            2: (4, 80),
            3: (65, 26),
            4: (92, 9),
            5: (83, 61),
            6: (22, 21),
            7: (97, 70),
            8: (20, 99),
            9: (66, 62)
        }
        self.city_groups = [
            [1, 4],
            [2, 6],
            [7],
            [5],
            [9],
            [8],
            [3]
        ]

    def calculate_euclidean_distance(self, coord1, coord2):
        return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

    def test_requirements(self):
        # Start and end at depot
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

        # Visit each group exactly once
        visited_groups = []
        for city in self.tour:
            for i, group in enumerate(self.city_groups):
                if city in group:
                    visited_groups.append(i)

        self.assertEqual(len(set(visited_groups)), len(self.city_groups))  # Unique groups check

        # Compute the total travel cost
        total_cost = 0
        for i in range(len(self.tour) - 1):
            t1 = self.city_coords[self.tour[i]]
            t2 = self.city_coords[self.tour[i + 1]]
            total_cost += self.calculate_euclidean_distance(t1, t2)

        self.assertAlmostEqual(total_cost, self.total_cost_provided, places=2)

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestRobotTour))
    return test_suite

runner = unittest.TextTestRunner()

if runner.run(suite()).wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")