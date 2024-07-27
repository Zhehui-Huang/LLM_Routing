import unittest
import math

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69),
            5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
        }
        self.groups = {
            0: [1, 2, 6],
            1: [3, 7, 8],
            2: [4, 5, 9]
        }
        self.tour = [0, 6, 7, 5, 0]
        self.expected_cost = 74.95

    def test_tour_starts_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_tour_visits_one_city_per_group(self):
        visited_groups = set()
        for city in self.tour[1:-1]:  # Ignore the depot city at the start and the end
            for group, cities in self.groups.items():
                if city in cities:
                    visited_groups.add(group)
        self.assertEqual(len(visited_groups), len(self.groups))

    def test_euclidean_distance_formula(self):
        def euclidean_distance(a, b):
            return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
        return euclidean_distance

    def test_total_travel_cost(self):
        total_distance = 0
        for i in range(len(self.tour) - 1):
            city_a_id = self.tour[i]
            city_b_id = self.tour[i + 1]
            city_a = self.cities[city_a_id]
            city_b = self.cities[city_b_id]
            distance = self.test_euclidean_distance_formula()(city_a, city_b)
            total_distance += distance
        self.assertAlmostEqual(total_distance, self.expected_cost, places=2)

def main():
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    test_suite.addTests(loader.loadTestsFromTestCase(TestRobotTour))

    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)

    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

if __name__ == "__main__":
    main()