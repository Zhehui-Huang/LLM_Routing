import unittest
from math import sqrt

def euclidean_distance(p1, p2):
    return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

class TestBTSPTour(unittest.TestCase):
    def setUp(self):
        # Given city coordinates
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
        
        self.expected_tour = [0, 14, 5, 9, 13, 10, 8, 6, 1, 4, 12, 3, 7, 11, 2, 0]
        self.expected_cost = 373.61498801130097
        self.expected_max_distance = 94.11163583744573

    def test_tour_start_and_end_at_depot(self):
        self.assertEqual(self.expected_tour[0], 0, "Tour should start at depot city 0")
        self.assertEqual(self.expected_tour[-1], 0, "Tour should end at depot city 0")

    def test_visit_each_city_once(self):
        unique_cities = set(self.expected_tour)
        self.assertEqual(len(unique_cities), 15, "Each city should be visited exactly once")

    def test_total_travel_cost(self):
        total_cost = 0
        for i in range(len(self.expected_tour) - 1):
            total_cost += euclidean_distance(self.cities[self.expected_tour[i]], self.cities[self.expected_tour[i + 1]])
        self.assertAlmostEqual(total_cost, self.expected_cost, msg="Total travel cost should match expected cost")

    def test_maximum_distance_between_consecutive_cities(self):
        max_distance = 0
        for i in range(len(self.expected_tour) - 1):
            distance = euclidean_per_distance(self.cities[self.expected_tour[i]], self.cities[self.expected_tour[i + 1]])
            if distance > max_distance:
                max_distance = distance
        self.assertAlmostEqual(max_distance, self.expected_max_distance, msg="Maximum distance between consecutive cities should match expected maximum")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBTSPTour)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")