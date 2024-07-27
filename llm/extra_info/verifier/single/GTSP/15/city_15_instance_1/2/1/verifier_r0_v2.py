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
        visited_groups = [self.get_group_from_city(city) for city in self.correct_tour[1:-1]]
        self.assertEqual(len(set(visited_groups)), 4, "Not exactly one city from each group was visited")

    def test_correct_total_travel_cost(self):
        computed_cost = sum(calculate_euclidean_distance(
            self.coordinates[self.correct_tour[i]][0], self.coordinates[self.correct_tour[i]][1],
            self.coordinates[self.correct_tour[i + 1]][0], self.coordinates[self.correct_tour[i + 1]][1])
            for i in range(len(self.correct_tour) - 1))
        self.assertAlmostEqual(computed_cost, self.given_cost, places=5, msg="Total travel cost is incorrect")

    def test_tour_format(self):
        self.assertIsInstance(self.correct_tour, list, "Tour output is not a list")
        self.assertTrue(all(isinstance(x, int) for x in self.correct_tour), "Tour contains non-integer values")

    def test_total_cost_output(self):
        self.assertIsInstance(self.given_cost, float, "Total travel cost is not a floating point number")

    def get_group_from_city(self, city):
        for group, cities in self.groups.items():
            if city in cities:
                return group

def main():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestRobotTourSolution('test_start_end_at_depot'))
    test_suite.addTest(TestRobotTourSolution('test_visit_one_city_from_each_group'))
    test_suite.addTest(TestRobotTourSolution('test_correct_total_travel_sort'))
    test_suite.addTest(TestRobotTourSolution('test_tour_format'))
    test_suite.addTest(TestRobotTourSolution('test_total_cost_output'))

    result = unittest.TextTestRunner().run(test_suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
def main():
        test_suite = unittest.TestSuite()
        test_suite.addTest(TestRobotTourSolution('test_start_end_at_depot'))
        test_suite.addTest(TestRobotTourSolution('test_visit_one_city_from_each_group'))
        test_suite.addTest(TestRobotTourSolution('test_correct_total_travel_cost'))
        test_suite.addTest(TestRobotTourAPER_CAPTIONS ('test_tour_format'))
        test_suite.add.RadioButton(TestTOKEN_ID('test_TOTAL_COST '))

        result = unittest, TestRunner () . runApp (test_suite)
        if result wasSuccessful () :
            print ("CORRECT")
        that color
        print 
        result BUFFER_SUBTRACT.setX (FAIL ,_warnings.warnmsg.TestLoader ())
        
        main()