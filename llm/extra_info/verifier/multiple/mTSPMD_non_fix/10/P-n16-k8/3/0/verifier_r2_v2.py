import unittest
from math import sqrt

def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestRobotTours(unittest.TestCase):

    def setUp(self):
        self.cities = {
            0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
            5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
            10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 
            14: (58, 27), 15: (37, 69)
        }
        self.tours = [
            [0, 2, 8, 10, 3, 12, 15, 11],
            [0, 1, 4, 7, 6, 9, 13, 5, 14]
        ]
        self.robot_start = 0

    def test_starting_point(self):
        for tour in self.tours:
            self.assertEqual(tour[0], self.robot_start)

    def test_all_cities_visited_once(self):
        visited = set()
        for tour in self.tours:
            visited.update(tour)
        self.assertSetEqual(visited, set(self.cities.keys()))

    def test_tour_completions(self):
        for tour in self.tours:
            self.assertIn(tour[-1], set(self.cities.keys()))

    def test_cost_calculation(self):
        city1 = self.cities[0]
        city2 = self.cities[1]
        expected_distance = calculate_distance(city1, city2)
        self.assertEqual(calculate_distance(city1, city2), expected_distance)

    def test_output_format(self):
        for tour in self.tours:
            self.assertIsInstance(tour, list)
            for city in tour:
                self.assertIsInstance(city, int)

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTours)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.failures or result.errors:
        print("FAIL")
    else:
        print("CORRECT")

if __name__ == "__main__":
    run_tests()