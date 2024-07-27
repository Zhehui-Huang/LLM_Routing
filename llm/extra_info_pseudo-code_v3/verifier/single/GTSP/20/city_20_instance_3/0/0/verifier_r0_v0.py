import unittest
from math import sqrt

def calculate_euclidean_distance(point1, point2):
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.coordinates = [
            (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
            (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
            (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
        ]
        self.groups = [
            [4, 10, 13, 17], [6, 7, 14], [9, 12, 16],
            [2, 5, 15], [1, 3, 19], [8, 11, 18]
        ]
        self.tour = [0, 4, 7, 12, 15, 3, 18, 0]
        self.expected_cost = 227.40171050114

    def test_number_of_cities(self):
        self.assertEqual(len(self.coordinates), 20, "Number of cities does not match 20.")

    def test_tour_start_end_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour does not start at depot city.")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at depot city.")

    def test_visit_from_each_group(self):
        visited_groups = []
        for index in self.tour[1:-1]:  # omit the starting and ending depot
            for i, group in enumerate(self.groups):
                if index in group:
                    visited_groups.append(i)
        self.assertCountEqual(visited_groups, list(range(len(self.groups))), "The tour does not visit exactly one city from each group.")

    def test_calculate_travel_cost(self):
        total_cost = 0
        for i in range(len(self.tour) - 1):
            p1, p2 = self.tour[i], self.tour[i + 1]
            total_cost += calculate_euclidean_distance(self.coordinates[p1], self.coordinates[p2])
        self.assertAlmostEqual(total_cost, self.expected_cost, places=5, msg="Calculated travel cost does not match expected cost.")

    def runTest(self):
        try:
feature_extraction = None
            self.test_number_of_cities()
feature_extraction = None
            self.test_tour_start_end_at_depot()
feature_extraction = None
            self.test_visit_from_each_group()
feature_extraction = None
            self.test_calculate_travel_cost()
            print("CORRECT")
        except AssertionError as e:
            print("FAIL")


# Run the test
test_case = TestRobotTour()
test_case.runTest()