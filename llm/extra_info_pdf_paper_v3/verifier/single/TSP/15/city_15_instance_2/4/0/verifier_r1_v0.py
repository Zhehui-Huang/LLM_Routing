import unittest
from math import sqrt

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        # City coordinates as provided
        self.cities = {
            0: (54, 87),
            1: (21, 84),
            2: (69, 84),
            3: (53, 40),
            4: (54, 42),
            5: (36, 30),
            6: (52, 82),
            7: (93, 44),
            8: (21, 78),
            9: (68, 14),
            10: (51, 28),
            11: (44, 79),
            12: (56, 58),
            13: (72, 43),
            14: (6, 99)
        }
        # Provided tour and cost
        self.tour = [0, 2, 0, 6, 11, 8, 1, 14, 0, 0, 0, 12, 4, 3, 10, 5, 0, 9, 0, 0, 0, 13, 7, 0, 0, 0, 0, 0, 0, 0]
        self.reported_cost = 554.01

    def test_tour_starts_and_ends_at_depot(self):
        # Requirement 1
        self.assertEqual(self.tour[0], 0, "Tour should start at depot")
        self.assertEqual(self.tour[-1], 0, "Tour should end at depot")

    def test_visit_all_cities_once(self):
        # Requirement 2
        city_counts = {i: self.tour.count(i) for i in range(1, 15)}
        for i in range(1, 15):
            self.assertEqual(city_counts[i], 1, f"City {i} should be visited exactly once")

    def test_distance_calculation(self):
        # Requirement 3
        def calculate_distance(city1, city2):
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            calculated_cost += calculate_distance(self.tour[i], self.tour[i+1])

        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=2, msg="Calculated cost should match the reported total travel cost")

    def test_output_format(self):
        # Requirement 5
        self.assertIsInstance(self.tour, list, "Tour should be a list")
        self.assertIsInstance(self.reported_cost, (float, int), "Total travel cost should be a number")
        self.assertTrue(all(isinstance(x, int) for x in self.tour), "All tour elements should be integers")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")