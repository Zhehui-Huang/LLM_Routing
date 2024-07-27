import unittest
import math

class TestKTSPSolution(unittest.TestCase):
    def setUp(self):
        # Given city coordinates with city 0 being the depot
        self.cities = {
            0: (8, 11),
            1: (40, 6),
            8: (61, 16),
            4: (25, 18)
        }
        # Solution tour and total travel cost
        self.tour = [0, 1, 8, 4, 0]
        self.reported_total_cost = 110.08796524611944

    def test_starts_and_ends_at_depot(self):
        # The tour should start and end at the depot city (city 0)
        self.assertEqual(self.tour[0], self.tour[-1], "Tour should start and end at city 0")

    def test_exactly_four_cities_visited(self):
        # Tour should visit exactly four cities
        self.assertEqual(len(set(self.tour)), 4, "Tour should visit exactly 4 distinct cities")

    def test_euclidean_distance(self):
        # Calculate total travel cost using Euclidean distance and compare with reported cost
        def euclidean_dist(city1, city2):
            return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

        calculated_cost = sum(euclidean_dist(self.cities[self.tour[i]], self.cities[self.tour[i + 1]]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(calculated_cost, self.reported_total_cost, places=5, msg="Calculated cost does not match reported cost")

unittest.main(argv=[''], verbosity=2, exit=False)