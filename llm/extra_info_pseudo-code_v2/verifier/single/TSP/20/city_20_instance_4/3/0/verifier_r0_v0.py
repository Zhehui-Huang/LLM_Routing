import unittest
from math import sqrt

class TestRobotTourSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), 
            (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), 
            (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54), 
            (64, 72), (14, 89)
        ]
        self.tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 15, 4, 3, 19, 0]
        self.reported_cost = 410.04

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_each_city_once(self):
        cities_visited = self.tour[1:-1]
        unique_cities_visited = set(cities_visited)
        self.assertEqual(len(cities_visited), len(unique_cities_visited))
        self.assertEqual(len(unique_cities_visited), 19)  # There are 19 cities excluding the depot

    def test_total_travel_cost(self):
        total_cost = 0
        for i in range(len(self.tour) - 1):
            city_a = self.cities[self.tour[i]]
            city_b = self.cities[self.tour[i + 1]]
            distance = sqrt((city_b[0] - city_a[0])**2 + (city_b[1] - city_a[1])**2)
            total_cost += distance
        
        self.assertAlmostEqual(total_cost, self.reported_cost, places=2)

    def test_output_includes_tour_and_cost(self):
        # This test is implicit in the setUp and the other test methods

        # Run the tests
unittest.main(argv=[''], verbosity=2, exit=False)