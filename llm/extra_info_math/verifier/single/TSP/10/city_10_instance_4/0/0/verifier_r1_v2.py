import math
import unittest

class TestTour(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (79, 15),
            1: (79, 55),
            2: (4, 80),
            3: (65, 26),
            4: (92, 9),
            5: (83, 61),
            6: (22, 21),
            7: (97, 70),
            8: (20, 99),
            9: (66, 62)
        }
        self.tour = [0, 4, 3, 1, 5, 7, 9, 8, 2, 6, 0]
        self.reported_cost = 337.1694332678818

    def test_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour does not start at the depot.")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at the depot.")

    def test_visits_each_city_once(self):
        visits = sorted(self.tour[1:-1])  # Exclude the repeated depot city at the end
        expected = list(range(1, 10))
        self.assertEqual(visits, expected, "Tour does not visit each city exactly once.")

    def calculate_euclidean_distance(self, from_city, to_city):
        x1, y1 = self.cities[from_city]
        x2, y2 = self.cities[to_city]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def test_correct_total_travel_cost(self):
        calculated_cost = sum(self.calculate_euclidean_distance(self.tour[i], self.tour[i+1]) for i in range(len(self.tour)-1))
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=5, msg="Reported travel cost is incorrect.")

# Run tests
if __name__ == "__main__":
    unittest.main()