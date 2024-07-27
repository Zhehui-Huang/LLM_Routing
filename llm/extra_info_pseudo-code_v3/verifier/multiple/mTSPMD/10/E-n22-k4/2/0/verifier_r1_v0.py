import unittest
from math import sqrt

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (145, 215),
            1: (151, 264),
            2: (159, 261),
            3: (130, 254),
            4: (128, 252),
            5: (163, 247),
            6: (146, 246),
            7: (161, 242),
            8: (142, 239),
            9: (163, 236),
            10: (148, 232),
            11: (128, 231),
            12: (156, 217),
            13: (129, 214),
            14: (146, 208),
            15: (164, 208),
            16: (141, 206),
            17: (147, 193),
            18: (164, 193),
            19: (129, 189),
            20: (155, 185),
            21: (139, 182)
        }
        self.tour = [0, 17, 17, 21, 16, 16, 16, 11, 6, 6, 7, 7, 7, 15, 16, 16, 16, 16, 16, 0]
        self.total_cost = 193.9760579266638

    def test_tour_length(self):
        """ Checks if the tour length is correct, accounting for all cities """
        self.assertEqual(22, len(set([city for city in self.tour if city not in [0]])) + 1)

    def test_all_cities_visited(self):
        """ Check if all cities are visited at least once."""
        visited = set(self.tour)
        self.assertEqual(set(range(22)), visited)

    def test_correct_start_and_end(self):
        """ Check if the tour starts and ends at the right depots """
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_travel_cost(self):
        """ Test if the computed travel cost matches the expected total """
        def calculate_distance(city1, city2):
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            return sqrt((x2 - x1)**2 + (y2 - y1)**2)

        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            calculated_cost += calculate_distance(self.tour[i], self.tour[i+1])

        self.assertAlmostEqual(calculated_cost, self.total_cost)

unittest.main(argv=[''], exit=False)