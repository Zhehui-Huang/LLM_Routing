import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestVRPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
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
        self.tour = [0, 3, 6, 4, 7, 2, 1, 9, 5, 8, 0]
        self.provided_cost = 354.91010610434057

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour does not start at depot city")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at depot city")

    def test_all_cities_visited_exactly_once(self):
        cities_visited = self.tour[1:-1]  # ignore starting and ending depot
        unique_cities_visited = set(cities_visited)
        self.assertEqual(len(unique_cities_visited), 9, "Not all cities visited exactly once")
        self.assertEqual(len(cities_visited), len(unique_cities_visited), "Some cities are visited more than once")

    def test_travel_cost(self):
        computed_cost = 0
        for i in range(len(self.tour)-1):
            city1 = self.tour[i]
            city2 = self.tour[i+1]
            computed_cost += calculate_distance(self.cities[city1], self.cities[city2])
        self.assertAlmostEqual(computed_cost, self.provided_cost, places=5, msg="Computed travel cost does not match the provided cost")

unittest.main(argv=[''], exit=False)