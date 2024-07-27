import unittest
from math import sqrt

def calculate_distance(city_a, city_b):
    return sqrt((city_b[0] - city_a[0])**2 + (city_b[1] - city_a[1])**2)

class TestKTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
            6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
            12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
            18: (64, 72), 19: (14, 89)
        }
        self.tour = [0, 15, 6, 10, 8, 17, 18, 13, 9, 12, 7, 16, 2, 11, 1, 19, 0]
        self.given_cost = 397.74265109264127

    def test_tour_length(self):
        # Checking for unique cities including the initial city (depot)
        self.assertEqual(len(set(self.tour)), 16, "The number of unique visited cities should be 16.")
    
    def test_tour_start_end(self):
        # Ensuring the tour starts and ends at the depot city
        self.assertEqual(self.tour[0], 0, "Tour should start at city 0.")
        self.assertEqual(self.tour[-1], 0, "Tour should end at city 0.")
    
    def test_cost_calculation(self):
        # Testing the travel cost against the given cost with precision
        calculated_cost = 0
        for i in range(1, len(self.tour)):
            city_a = self.tour[i - 1]
            city_b = self.tour[i]
            calculated_cost += calculate_distance(self.cities[city_a], self.cities[city_b])
        self.assertAlmostEqual(calculated_cost, self.given_cost, places=5, "The calculated travel cost should match the given total travel cost.")

if __name__ == "__main__":
    unittest.main()