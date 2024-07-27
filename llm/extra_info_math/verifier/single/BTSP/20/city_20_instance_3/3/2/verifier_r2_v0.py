import unittest
from math import sqrt

# Given city coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Euclidean distance calculator
def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestVerifyTour(unittest.TestCase):
    def setUp(self):
        # Given tour and parameters
        self.tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
        self.total_travel_cost = 458.36719998557066
        self.maximum_distance = 68.15423684555495
    
    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour does not start at depot")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at depot")
    
    def test_visit_all_cities_exactly_once(self):
        # All cities except the depot (0) included from 1 to 19
        visited_cities = sorted(set(self.tour) - {0})
        self.assertListEqual(visited_cities, list(range(1, 20)), "Visit all cities constraint failed")
    
    def test_travel_cost(self):
        calculated_cost = sum(calculate_distance(cities[self.tour[i]], cities[self.tour[i + 1]]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(calculated_cost, self.total_travel_cost, places=8, msg="Total travel cost is incorrect")
    
    def test_maximum_distance(self):
        measured_max_distance = max(calculate_distance(cities[self.tour[i]], cities[self.tour[i+1]]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(measured_max_distance, self.maximum_distance, places=8, msg="Maximum distance between consecutive cities is incorrect")
    
    def test_conclusion(self):
        try:
            self.test_tour_starts_and_ends_at_depot()
            self.test_visit_all_cities_exactly_once()
            self.test_travel_cost()
            self.test_maximumdomestic_distance()
            print("CORRECT")
        except AssertionError:
            print("FAIL")

# Instantiate the test case
test_case = TestVerifyTour()
test_case.test_conclusion()