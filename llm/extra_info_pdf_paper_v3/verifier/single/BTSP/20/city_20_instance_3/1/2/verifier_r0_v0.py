import unittest
from math import sqrt

# Let's define the cities coordinates.
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), 
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0), 
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), 
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

def calculate_distance(c1, c2):
    """ Calculate Euclidean distance between two points. """
    return sqrt((c2[0] - c1[0]) ** 2 + (c2[1] - c1[1]) ** 2)

class TestTourSolution(unittest.TestCase):

    def setUp(self):
        self.tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
        self.total_cost = 458.36719998557066
        self.max_distance = 68.15423684555495

    def test_tour_starting_ending_city(self):
        """ Test the tour starts and ends at depot city 0. """
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_each_city_once(self):
        """ Test every city except the depot must be visited exactly once. """
        tour_without_depots = self.tour[1:-1]
        unique_cities = set(tour_without_depots)
        self.assertEqual(len(unique_cities), 19)

    def test_total_travel_cost(self):
        """ Test the total cost of the trip based on the Euclidean distance. """
        calc_cost = sum(calculate_distance(cities[self.tour[i]], cities[self.tour[i + 1]]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(calc_cost, self.total_cost, places=5)

    def test_max_distance_between_consecutive_cities(self):
        """ Test the maximum distance between consecutive cities. """
        dists = [calculate_distance(cities[self.tour[i]], cities[self.tour[i + 1]]) for i in range(len(self.tour) - 1)]
        self.assertAlmostEqual(max(dists), self.max_distance, places=5)

    def test_tour_output_format(self):
        """ Test output format includes tour, total cost and max consecutive distance. """
        self.assertIsInstance(self.tour, list)
        self.assertIsInstance(self.total_cost, float)
        self.assertIsInstance(self.max_distance, float)

# Running the tests
if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)