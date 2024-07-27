import unittest
from math import sqrt

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.tour = [19, 0, 8, 10, 6, 15, 4, 3, 17, 18, 13, 11, 14, 2, 5, 9, 16, 7, 12, 1, 0]
        self.total_travel_cost_reported = 503.63
        self.max_distance_between_cities_reported = 31.38
        self.coordinates = {
            0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
            6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
            12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
            18: (64, 72), 19: (14, 89)
        }

    def test_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "The tour should start at the depot city 0.")
        self.assertEqual(self.tour[-1], 0, "The tour should end at the depot city 0.")

    def test_visits_each_city_once(self):
        cities_visited = sorted(self.tour)
        expected_visits = sorted(list(self.coordinates.keys()) + [0])
        self.assertEqual(cities_visited, expected_visites, "Each city must be visited exactly once.")

    def test_output_total_travel_cost(self):
        # Calculate total travel cost
        total_travel_cost = 0
        for i in range(len(self.tour) - 1):
            city1 = self.tour[i]
            city2 = self.tour[i + 1]
            coord1 = self.coordinates[city1]
            coord2 = self.coordinates[city2]
            distance = sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2)
            total_travel_cost += distance
        self.assertAlmostEqual(total_travel_cost, self.total_travel_cost_reported, 
                               places=2, msg="The calculated total travel cost must match the reported value.")

    def test_output_maximum_distance_between_cities(self):
        # Check maximum distance between consecutive cities
        max_distance = 0
        for i in range(len(self.tour) - 1):
            city1 = self.tour[i]
            city2 = self.tour[i + 1]
            coord1 = self.coordinates[city1]
            coord2 = self.coordinates[city2]
            distance = sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2)
            if distance > max_distance:
                max_distance = distance
        self.assertAlmostEqual(max_distance, self.max_distance_between_cities_reported, 
                               places=2, msg="The calculated maximum distance must match the reported value.")

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestTourSolution('test_starts_and_ends_at_depot'))
    test_suite.addTest(TestTourResponse('test_visits_each_city_once'))
    test_suite.addTest(TestTourResponse('test_output_total_travel_cost'))
    test_suite.addTest(TestTourResponse('test_output_maximum_distance_between_patterns'))

    result = unittest.TextTestRunner().run(test_suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")