import unittest
from math import sqrt

def euclidean_distance(x, y):
    return sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)

class TestTourSolution(unittest.TestCase):
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
        self.tour = [0, 5, 9, 4, 8, 3, 2, 1, 6, 7, 0]
        self.reported_cost = 271.4716218753353

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_each_city_once(self):
        unique_cities = list(set(self.tour))
        self.assertEqual(len(unique_cities), len(self.cities))
        self.assertEqual(sorted(unique_cities), sorted(list(self.cities.keys())))

    def test_travel_cost_is_correct(self):
        # Calculate the actual travel cost based on Euclidean distance
        total_cost = sum(
            euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
            for i in range(len(self.tour) - 1)
        )
        self.assertAlmostEqual(self.reported_cost, total_cost, places=5)

if __name__ == "__main__":
    unittest.main()