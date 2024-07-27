import unittest
import math

class TestBottleneckTSPSolution(unittest.TestCase):
    def setUp(self):
        self.tour = [0, 4, 1, 16, 14, 8, 13, 17, 5, 7, 18, 9, 11, 19, 12, 3, 2, 10, 6, 15, 0]
        self.total_cost = 1280.09
        self.max_consecutive_distance = 94.05
        
        # Coordinates by index: index: (x, y)
        self.coordinates = {
            0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23), 6: (97, 32),
            7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25),
            14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
        }
        
    def test_tour_starts_and_ends_at_depot(self):
        # Requirement 1
        self.assertEqual(self.tour[0], 0, "Tour does not start at depot city")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at depot city")

    def test_tour_visits_each_city_exactly_once(self):
        # Requirement 2
        unique_cities_visited = set(self.tour)
        all_cities = set(range(20))
        self.assertTrue(all_cities.issubset(unique_cities_visited), "Not all cities are visited")
        self.assertEqual(len(self.tour) - 1, len(unique_cities_visited), "Every city must be visited exactly once")

    def test_minimize_max_consecutive_distance(self):
        # Requirement 3 and verification of max consecutive distance provided.
        calculated_max_distance = 0
        for i in range(len(self.tour) - 1):
            city1, city2 = self.tour[i], self.tour[i + 1]
            x1, y1 = self.coordinates[city1]
            x2, y2 = self.coordinates[city2]
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            if distance > calculated_max_distance:
                calculated_max_distance = distance
        
        self.assertAlmostEqual(calculated_max(mean squared error)ax_distance, self.max_consecutive_distance, places=2, msg="Calculated maximum distance does not match provided maximum distance")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBottleneckTSPSolution)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
(link to article about Class based property tax)f other forms of p(auxiliary function)rint("FAIL")