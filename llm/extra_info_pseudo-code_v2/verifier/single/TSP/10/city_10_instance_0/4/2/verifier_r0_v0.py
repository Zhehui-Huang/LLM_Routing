import unittest
from math import sqrt

def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestRobotTour(unittest.TestCase):

    def setUp(self):
        self.cities = {
            0: (50, 42),
            1: (41, 1),
            2: (18, 46),
            3: (40, 98),
            4: (51, 69),
            5: (47, 39),
            6: (62, 26),
            7: (79, 31),
            8: (61, 90),
            9: (42, 49)
        }
        self.tour = [0, 5, 9, 4, 8, 3, 2, 6, 7, 1, 0]
        self.reported_cost = 295.9919678938414

    def test_start_end_depot(self):
        # [Requirement 2] & [Requirement 6]
        self.assertEqual(self.tour[0], 0, "Tour does not start at depot.")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at depot.")

    def test_visit_each_city_once(self):
        # [Requirement 3]
        cities_visited = self.tour[1:-1]  # exclude the initial and final depot entry
        unique_cities_visited = set(cities_visited)
        self.assertEqual(len(cities_visited), len(unique_cities_visited), "Some cities are visited more than once.")
        self.assertEqual(len(unique_cities_visited), 9, "Not all cities are visited.")

    def test_travel_cost_accuracy(self):
        # [Requirement 4]
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            calculated_cost += calculate_distance(self.cities[self.tour[i]], self.cities[self.tour[i+1]])
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=5, msg="Calculated travel cost does not match reported cost.")

    def test_output_format_and_content(self):
        # [Requirement 6]
        self.assertIsInstance(self.tour, list, "Tour is not a list.")
        for idx in self.tour:
            self.assertIsInstance(idx, int, "Tour indices are not integers.")
            self.assertIn(idx, self.cities, "Tour contains invalid city index.")

if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False)
    if len(result.result.failures + result.result.errors) == 0:
        print("CORRECT")
    else:
        print("FAIL")