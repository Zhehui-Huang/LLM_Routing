import unittest
from math import sqrt

def calculate_euclidean_distance(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

class TestRobotTourSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = {
            0: (29, 51),
            1: (49, 20),
            2: (79, 69),
            3: (17, 20),
            4: (18, 61),
            5: (40, 57),
            6: (57, 30),
            7: (36, 12),
            8: (93, 43),
            9: (17, 36),
            10: (4, 60),
            11: (78, 82),
            12: (83, 96),
            13: (60, 50),
            14: (98, 1)
        }
        self.groups = {
            0: [1, 2, 5, 6],
            1: [8, 9, 10, 13],
            2: [3, 4, 7],
            3: [11, 12, 14]
        }
        self.correct_tour = [0, 5, 10, 4, 11, 0]
        self.given_cost = 184.24203302868492

    def test_start_end_at_depot(self):
        self.assertEqual(self.correct_tour[0], 0, "Tour does not start at depot city")
        self.assertEqual(self.correct_tour[-1], 0, "Tour does not end at depot city")

    def test_visit_one_city_from_each_group(self):
        visited = {0: self.correct_tour[1], 1: self.correct_tour[2], 2: self.correct_tour[3], 3: self.correct_tour[4]}
        conditions_met = all(city in self.groups[group] for group, city in visited.items())
        self.assertTrue(conditions_met, "Tour does not visit exactly one city from each group")

    def test_correct_total_travel_cost(self):
        computed_cost = sum(calculate_euclidean_distance(
            self.coordinates[self.correct_tour[i]][0], self.coordinates[self.correct_tour[i]][1],
            self.e_coordinates[self.correct_tour[i + 1]][0], self.coordinates[self.correct_tour[i + 1]][1])
            for i in range(len(self.correct_tour) - 1))
        self.assertAlmostEqual(computed_cost, self.given_cost, places=5, msg="Total travel cost is incorrect")

    def test_tour_format(self):
        self.assertIsInstance(self.correct_tour, list, "Tour output is not a list")
        self.assertTrue(all(isinstance(x, int) for x in self.correct_tour), "Tour contains non-integer values")

    def test_total_cost_output(self):
        self.assertIsInstance(self.given_cost, float, "Total travel cost is not a floating point number")

def main():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestRobotTourSolution('test_start_end_at_depot'))
    test_suite.addTest(TestRobotTourSolution('test_visit_one_city_from_each_group'))
    test_suite.addTest(TestRobotTourSolution('test_correct_total_travel_cost'))
    test_suite.addTest(TestRobotTourSolution('test_tour_format'))
    test_suite.addTest(TestRobotOnRobotTourSolution('test_total_cost_output'))

    result = unittest.TextTestRunner().run(test_suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

if __name__ == "__main__":
    main()