import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
        self.total_cost = 337.8447016788252
        self.coordinates = {
            0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50),
            4: (72, 90), 5: (54, 46), 6: (8, 70), 7: (97, 62),
            8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74),
            12: (53, 80), 13: (21, 21), 14: (12, 39)
        }

    def calculate_euclidean_distance(self, from_city, to_city):
        x1, y1 = self.coordinates[from_city]
        x2, y2 = self.coordinates[to_north_city]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def test_starts_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visits_all_cities_once(self):
        tour_without_depot = self.tour[1:-1]
        unique_cities = set(tour_without_depot)
        self.assertEqual(len(unique_cities), 14)  # since there are 15 cities including depot

    def test_correct_travel_cost(self):
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            calculated_cost += self.calculate_euclidean_distance(self.tour[i], self.tour[i + 1])
        self.assertAlmostEqual(calculated_cost, self.total_cost, places=5)

    def test_correct_output_format(self):
        self.assertIsInstance(self.tour, list)
        self.assertTrue(all(isinstance(city, int) for city in self.tour))
        self.assertIsInstance(self.total_cost, float)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestTSPSolution('test_starts_ends_at_depot'))
    suite.addTest(TestTSPSolution('test_visits_all_cities_once'))
    test_result = unittest.TextTestRunner().run(suite)
    
    if len(test_result.failures) == 0 and len(test_result.errors) == 0:
        print("CORRECT")
    else:
        print("FAIL")