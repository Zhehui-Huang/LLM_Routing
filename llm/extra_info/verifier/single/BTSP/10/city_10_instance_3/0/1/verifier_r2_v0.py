import math
import unittest

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (84, 67),  # city 0
            (74, 40),  # city 1
            (71, 13),  # city 2
            (74, 82),  # city 3
            (97, 28),  # city 4
            (0, 31),   # city 5
            (8, 62),   # city 6
            (74, 56),  # city 7
            (85, 71),  # city 8
            (6, 76)    # city 9
        ]
        self.tour = [0, 8, 3, 9, 5, 6, 7, 1, 2, 4, 0]
        self.reported_total_cost = 345.92
        self.reported_max_distance = 68.26

    def test_start_and_end_at_depot(self):
        # Requirement 1
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_each_city_once(self):
        # Requirement 2
        expected_visits = set(range(len(self.cities)))
        actual_visits = set(self.tour[1:-1])
        self.assertEqual(actual_visits, expected_visits)

    def test_output_tour_format(self):
        # Requirement 5
        self.assertEqual(self.tour[0], self.tour[-1])

    def test_calculate_total_travel_cost(self):
        # Requirement 6
        total_cost = 0
        for i in range(len(self.tour) - 1):
            total_cost += euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
        self.assertAlmostEqual(total_cost, self.reported_total_cost, places=2)

    def test_max_distance_between_cities(self):
        # Requirement 7
        max_distance = 0
        for i in range(len(self.tour) - 1):
            dist = euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
            if dist > max_distance:
                max_distance = dist
        self.assertAlmostEqual(max_distance, self.reported_max_distance, places=2)

if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
    test_results = unittest.TextTestRunner().run(test_suite)
    if test_results.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")