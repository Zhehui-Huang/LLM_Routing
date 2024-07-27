import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestBTSPSolution(unittest.TestCase):
    cities = [
        (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
        (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
        (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
        (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
    ]
    tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
    expected_total_cost = 458.36719998557066
    expected_max_distance = 68.15423684555495

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_each_city_visited_exactly_once(self):
        visited = set(self.tour)
        expected_cities = set(range(len(self.cities)))
        self.assertEqual(visited, expected_cities)

    def test_total_travel_cost(self):
        total_cost = sum(calculate_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
                         for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(total_cost, self.expected_total_cost)

    def test_max_distance_between_consecutive_cities(self):
        max_distance = max(calculate_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
                           for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(max_distance, self.expected_max_distance)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestBTSPSolution))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

if __name__ == '__main__':
    run_tests()