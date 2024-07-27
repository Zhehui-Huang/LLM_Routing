import math
import unittest

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
            5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
            10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
        }
        self.tour = [8, 10, 12, 4, 9, 2, 5, 1, 0, 6, 3, 14, 0]
        self.expected_cost = 269.42

    def euclidean_distance(self, city1, city2):
        return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
    
    def calculate_total_distance(self, tour):
        total_distance = 0
        for i in range(len(tour) - 1):
            city1 = self.cities[tour[i]]
            city2 = self.cities[tour[i + 1]]
            total_distance += self.euclidean_distance(city1, city2)
        return round(total_distance, 2)
    
    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
    
    def test_tour_length(self):
        self.assertEqual(len(set(self.tour)), 12)  # Unique cities including depot
    
    def test_tour_cost(self):
        calculated_cost = self.calculate_total_distance(self.tour)
        self.assertEqual(calculated_cost, self.expected_cost)  # Rounded two decimal places
    
    def test_all_cities_are_available(self):
        used_cities = set(self.tour)
        all_cities = set(self.cities.keys())
        self.assertTrue(used_cities.issubset(all_cities))

if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
    test_results = unittest.TextTestRunner().run(test_suite)
    
    if test_results.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")