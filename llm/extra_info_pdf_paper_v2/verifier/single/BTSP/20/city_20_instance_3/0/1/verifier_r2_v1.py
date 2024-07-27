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
        # Check both the start and end are the depot city (city 0)
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_each_city_visited_exactly_once(self):
        # Check each city is visited exactly once except the depot which is visited twice (start/end)
        # Deep copy of tour excluding first occurrence of city 0
        visit_verify = self.tour[1:-1]
        all_cities = set(range(1, len(self.cities)))  # City indices excluding the depot
        self.assertEqual(set(visit_verify), all_cities)

    def test_total_travel_cost(self):
        total_cost = sum(calculate_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(total_cost, self.expected_total_cost, places=5)

    def test_max_distance_between_consecutive_cities(self):
        max_distance = max(calculate_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(max_distance, self.expected_max_distance, places=5)

# Running the tests outside of a normal testing context
if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestBTSPSolution))