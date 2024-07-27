import unittest
from math import sqrt

def calculate_euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
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
        self.tour = [0, 3, 6, 4, 7, 2, 1, 9, 5, 8, 0]
        self.reported_total_cost = 354.91010610434057

    def test_start_and_end_at_depot(self):
        self.assertEqual(self.tour[0], 0, "The tour should start at the depot city (city 0).")
        self.assertEqual(self.tour[-1], 0, "The tour should end at the depot city (city 0).")

    def test_visit_each_city_once(self):
        unique_cities = set(self.tour)
        self.assertEqual(len(unique_cities), 10, "The robot should visit each city exactly once, including the depot.")
        for city in range(10):  # City indices are from 0 to 9
            self.assertIn(city, unique_cities, f"City {city} should be visited.")

    def test_total_cost_calculation(self):
        computed_total_cost = 0
        for i in range(len(self.tour) - 1):
            computed_total_cost += calculate_euclidean_distance(
                self.cities[self.tour[i]], self.cities[self.tour[i + 1]]
            )
        self.assertAlmostEqual(computed_total_cost, self.reported_total_cost, places=5,
                               msg="Computed total cost should match the provided total travel cost.")

    def test_output_format(self):
        self.assertTrue(isinstance(self.tour, list) and all(isinstance(x, int) for x in self.tour),
                        "Tour should be a list of integers.")
        self.assertTrue(isinstance(self.reported_total_cost, float), "Total travel cost should be of type float.")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTSPSolution))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    correct = result.wasSuccessful()
    print("CORRECT" if correct else "FAIL")