import unittest
from math import sqrt

def calculate_euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = {
            0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
            5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
            10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
            15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
        }
        self.groups = [
            [5, 6, 16], [8, 18, 19], [11, 12, 13],
            [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]
        ]
        self.proposed_tour = [0, 5, 18, 13, 1, 14, 10, 15, 0]
        self.proposed_cost = 266.71610174713

    def test_start_and_end_at_depot(self):
        self.assertEqual(self.proposed_tour[0], 0)
        self.assertEqual(self.proposed_tour[-1], 0)

    def test_one_city_from_each_group(self):
        # Extract the visited cities from the proposed tour (exclude depot)
        visited_cities = set(self.proposed_tour[1:-1])
        visited_once_for_each_group = all(len(visited_cities.intersection(group)) == 1 for group in self.groups)
        self.assertTrue(visited_once_for_each_group)

    def test_euclidean_travel_cost(self):
        total_cost = 0
        for i in range(len(self.proposed_tour) - 1):
            city1, city2 = self.proposed_tour[i], self.proposed_tour[i + 1]
            total_cost += calculate_euclidean_distance(self.coordinates[city1], self.coordinates[city2])
        self.assertAlmostEqual(total_cost, self.proposed_cost, places=5)

    def test_correct_tour_output(self):
        self.assertTrue(len(self.proposed_tour) >= 9)  # Including depot start and end
        self.assertTrue(all(isinstance(city, int) for city in self.proposed_tour))

    def test_correct_cost_output(self):
        self.assertIsInstance(self.proposed_cost, float)

def main():
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
    test_result = unittest.TextTestRunner().run(test_suite)
    
    if test_result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")
        for fail in test_result.failures + test_result.errors:
            print(fail[1])

if __name__ == "__main__":
    main()