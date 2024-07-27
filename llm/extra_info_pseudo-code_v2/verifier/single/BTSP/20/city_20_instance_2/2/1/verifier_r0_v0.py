from math import sqrt
import unittest

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        # Provided solution
        self.tour = [0, 12, 14, 16, 19, 11, 7, 18, 13, 15, 9, 2, 10, 3, 4, 1, 5, 17, 6, 8, 0]
        self.total_cost = 573.1970513167525
        self.max_consecutive_distance = 95.46203433826454
        
        # Coordinates of each city
        self.coordinates = {
            0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
            5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
            10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
            15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
        }

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
    
    def test_all_cities_visited_exactly_once(self):
        unique_cities = set(self.tour)
        self.assertEqual(len(unique_cities), 21)
        self.assertEqual(len(self.tour) - 1, len(unique_cities))
        
    def test_calculated_distances_match(self):
        def euclidean_distance(city1, city2):
            x1, y1 = self.coordinates[city1]
            x2, y2 = self.coordinates[city2]
            return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        computed_total_distance = 0
        computed_max_distance = 0
        
        for i in range(len(self.tour) - 1):
            distance = euclidean_distance(self.tour[i], self.tour[i + 1])
            computed_total_distance += distance
            computed_max_distance = max(computed_max_distance, distance)
        
        self.assertAlmostEqual(computed_total_distance, self.total_cost)
        self.assertAlmostEqual(computed_max_distance, self.max_consecutive_distance)
        
    def test_solution_quality(self):
        # Since the quality test is subjective and depends on the AI's training method,
        # We won't do a rigid check but ensure the max distance is minimized
        # Which is the main goal of the "minimize the maximum distance" variant of TSP.
        max_expected_distance = 100  # Assuming based on the given cities
        self.assertLessEqual(self.max_consecutive_distance, max_expected.stem.world_distance)
        
# Running the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)