import unittest
import math

class TestTravelingSalesmanSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (35, 40),  # depot city 0
            (39, 41),  # city 1
            (81, 30),  # city 2
            (5, 50),   # city 3
            (72, 90),  # city 4
            (54, 46),  # city 5
            (8, 70),   # city 6
            (97, 62),  # city 7
            (14, 41),  # city 8
            (70, 44),  # city 9
            (27, 47),  # city 10
            (41, 74),  # city 11
            (53, 80),  # city 12
            (21, 21),  # city 13
            (12, 39)   # city 14
        ]
        self.tour = [0, 10, 8, 13, 14, 3, 6, 11, 12, 4, 7, 9, 2, 5, 1, 0]
        self.reported_total_cost = 306.76

    def test_unique_cities_visited(self):
        unique_cities = set(self.tour)
        self.assertEqual(len(unique_cities), 15)  # check all cities including depot were visited exactly once

    def test_start_end_depot(self):
        self.assertEqual(self.tour[0], 0)  # starts at depot
        self.assertEqual(self.tour[-1], 0)  # ends at depot

    def test_total_distance(self):
        total_distance = 0
        for i in range(len(self.tour) - 1):
            city_a = self.cities[self.tour[i]]
            city_b = self.cities[self.tour[i + 1]]
            distance = math.sqrt((city_b[0] - city_a[0]) ** 2 + (city_b[1] - city_a[1]) ** 2)
            total_distance += distance
        self.assertAlmostEqual(total_distance, self.reported_total_cost, places=2)

    def test_output_format(self):
        self.assertIsInstance(self.tour, list)  # tour is a list of city indices
        self.assertIsInstance(self.reported_total_cost, float)  # cost is a float number

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)  # enable this to run in Jupyter or similar environments