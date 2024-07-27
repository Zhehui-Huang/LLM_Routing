import unittest
from math import sqrt

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (16, 90),
            1: (43, 99),
            2: (80, 21),
            3: (86, 92),
            4: (54, 93),
            5: (34, 73),
            6: (6, 61),
            7: (86, 69),
            8: (30, 50),
            9: (35, 73),
            10: (42, 64),
            11: (64, 30),
            12: (70, 95),
            13: (29, 64),
            14: (32, 79)
        }
        self.groups = [
            {1, 6, 14},
            {5, 12, 13},
            {7, 10},
            {4, 11},
            {2, 8},
            {3, 9}
        ]
        self.proposed_tour = [0, 14, 5, 10, 11, 8, 9, 0]
        self.proposed_cost = 166.75801920718544

    def test_cities_count(self):
        self.assertEqual(len(self.cities), 15)
        
    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.proposed_tour[0], 0)
        self.assertEqual(self.proposed_tour[-1], 0)

    def test_exact_one_city_per_group(self):
        visited = set(self.proposed_tour[1:-1])  # exclude the depot city
        for group in self.groups:
            self.assertEqual(len(visited.intersection(group)), 1)

    def test_output_tour_with_city_indices(self):
        self.assertIsInstance(self.proposed_tour, list)
        self.assertTrue(all(isinstance(city, int) for city in self.proposed_tour))

    def test_travel_cost_is_correct(self):
        def euclidean_distance(city1, city2):
            return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

        calc_cost = 0
        for i in range(len(self.proposed_tour) - 1):
            start_city = self.proposed_tour[i]
            end_city = self.proposed_tour[i+1]
            calc_cost += euclidean_distance(self.cities[start_city], self.cities[end_city])

        self.assertAlmostEqual(calc_cost, self.proposed_cost, places=5)

    def test_check_output_cost_format(self):
        self.assertIsInstance(self.proposed_cost, float)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestTSPSolution))
    
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")