import unittest
import math

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        # Define city coordinates
        self.cities = {
            0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92),
            4: (54, 93), 5: (34, 73), 6: (6, 61), 7: (86, 69),
            8: (30, 50), 9: (35, 73), 10: (42, 64), 11: (64, 30),
            12: (70, 95), 13: (29, 64), 14: (32, 79)
        }
        # Grouping cities
        self.groups = [
            [1, 6, 14], [5, 12, 13], [7, 10], [4, 11], 
            [2, 8], [3, 9]
        ]
        # The provided tour and its cost
        self.tour = [0, 10, 11, 2, 3, 12, 1, 0]
        self.reported_cost = 238.9111036098412

    def test_tour_begins_and_ends_at_depot(self):
        """ The tour should start and end at the depot city """
        self.assertEqual(self.tour[0], 0, "Tour should start at depot city 0.")
        self.assertEqual(self.tour[-1], 0, "Tour should end at depot city 0.")

    def test_tour_visits_one_city_from_each_group(self):
        """ Each city group should be represented exactly once in the tour (excluding depot) """
        tour_groups = []
        for city in self.tour[1:-1]:  # Exclude starting and ending depot
            for i, group in enumerate(self.groups):
                if city in group:
                    tour_groups.append(i)
        self.assertEqual(len(set(tour_groups)), len(self.groups), "Tour should visit one city from each group.")

    def test_total_travel_cost(self):
        """ Verify if the calculated travel cost matches the reported cost """
        total_cost = 0
        for i in range(1, len(self.tour)):
            start = self.cities[self.tour[i - 1]]
            end = self.cities[self.tour[i]]
            distance = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
            total_cost += distance
        self.assertAlmostEqual(total_cost, self.reported_cost, places=5, msg="Calculated cost does not match reported cost.")

def run_tests():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestTourSolution('test_tour_begins_and_ends_at_depot'))
    test_suite.addTest(TestTourSolution('test_tour_visits_one_city_from_each_group'))
    test_suite.addTest(TestTourSolution('test_total_travel_cost'))
    runner = unittest.TextTestRunner()
    runner.run(test_suite)

run_tests()