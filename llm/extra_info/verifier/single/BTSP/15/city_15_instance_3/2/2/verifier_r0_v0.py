import math
import unittest

class TestTourSolution(unittest.TestCase):
    cities = [
        (16, 90),  # Depot city 0
        (43, 99),
        (80, 21),
        (86, 92),
        (54, 93),
        (34, 73),
        (6, 61),
        (86, 69),
        (30, 50),
        (35, 73),
        (42, 64),
        (64, 30),
        (70, 95),
        (29, 64),
        (32, 79)
    ]

    def setUp(self):
        self.tour = [0, 14, 5, 9, 1, 13, 6, 10, 4, 8, 12, 3, 7, 11, 2, 0]
        self.total_cost = 488.32
        self.max_distance = 94.11

    def test_tour_start_end_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_each_city_once(self):
        cities_visited = set(self.tour)
        self.assertEqual(len(cities_visited), len(self.cities))  # Includes depot city visited twice

    def test_calculate_total_cost(self):
        calculated_cost = sum(math.sqrt((self.cities[self.tour[i]][0] - self.cities[self.tour[i+1]][0])**2 +
                                        (self.cities[self.tour[i]][1] - self.cities[self.tour[i+1]][1])**2)
                               for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(calculated_cost, self.total_cost, places=2)

    def test_calculate_max_distance(self):
        calculated_max_distance = max(
            math.sqrt((self.cities[self.tour[i]][0] - self.cities[self.tour[i+1]][0])**2 +
                      (self.cities[self.tour[i]][1] - self.cities[self.tour[i+1]][1])**2)
            for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(calculated_max_distance, self.max_distance, places=2)

# Run the unit tests
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTourSolution)
    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")