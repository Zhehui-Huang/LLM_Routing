import unittest
from math import sqrt

def calculate_euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates of the cities
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
        # Provided solution
        self.tour = [0, 8, 5, 2, 1, 9, 0]
        self.provided_cost = 183.85354044487238

    def test_start_and_end_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour does not start at the depot city.")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at the depot city.")

    def test_exact_six_cities_included(self):
        unique_cities = set(self.tour)
        self.assertEqual(len(unique_cities), 6, "Tour does not include exactly 6 unique cities.")

    def test_total_travel_cost(self):
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            city1 = self.tour[i]
            city2 = self.tour[i+1]
            calculated_cost += calculate_euclidean_distance(self.cities[city1], self.cities[city2])
        
        # Testing the provided cost is somewhat tricky without the exact algorithm used initially, assuming it's correct:
        self.assertAlmostEqual(calculated_cost, self.provided_cost, places=5, msg="Calculated total travel cost does not match the provided cost.")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)