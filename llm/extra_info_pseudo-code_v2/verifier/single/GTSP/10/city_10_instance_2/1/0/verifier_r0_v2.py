from math import sqrt
import unittest

class TestRobotTour(unittest.TestCase):
    cities = {
        0: (90, 3),
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
    tour_solution = [0, 6, 8, 4, 1, 2, 0]
    tour_cost_solution = 355.80123069874605

    def test_all_conditions(self):
        # Check tour starts and ends at the depot
        self.assertEqual(self.tour_solution[0], 0, "Tour does not start at depot")
        self.assertEqual(self.tour_solution[-1], 0, "Tour does not end at depot")

        # Check the tour visits exactly one city from each group
        visited_groups = [False] * len(self.groups)
        for city in self.tour_solution:
            for i, group in enumerate(self.groups):
                if city in group:
                    if visited_groups[i]:
                        self.fail("Group {} visited more than once.".format(i))
                    visited_groups[i] = True

        self.assertTrue(all(visited_groups), "Not all groups were visited.")
        
        # Check the total travel cost calculation
        def euclidean_distance(city1, city2):
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        tour_cost_calculated = 0
        for i in range(len(self.tour_solution) - 1):
            tour_cost_calculated += euclidean_distance(self.tour_solution[i], self.tour_solution[i + 1])

        self.assertAlmostEqual(tour_cost_calculated, self.tour_cost_solution, places=5, msg="Calculated tour cost does not match provided solution")

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestRobotTour('test_all_conditions'))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

run...";