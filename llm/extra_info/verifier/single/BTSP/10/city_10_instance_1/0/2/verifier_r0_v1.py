import math
import unittest

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        # City coordinates
        self.cities = [
            (53, 68),  # Depot
            (75, 11),
            (91, 95),
            (22, 80),
            (18, 63),
            (54, 91),
            (70, 14),
            (97, 44),
            (17, 69),
            (95, 89)
        ]
        # Provided solution
        self.tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]
        self.reported_cost = 291.41088704894975
        self.reported_max_distance = 56.61271941887264

    def test_path_starts_and_ends_at_depot(self):
        # Test if tour starts and ends at the depot
        self.assertEqual(self.tour[0], 0, "Tour does not start at depot.")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at depot.")

    def test_visits_each_city_exactly_once(self):
        # Test if each city is visited exactly once
        unique_cities = set(self.tour[1:-1])
        self.assertEqual(len(unique_cities), 9, "Does not visit each city exactly once.")
        
    def test_correct_calculation_of_distances(self):
        # Test if total cost and maximum distance are calculated correctly
        def euclidean_distance(a, b):
            return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
        
        actual_cost = 0
        max_distance = 0
        for i in range(len(self.tour) - 1):
            distance = euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
            actual_cost += distance
            max_distance = max(max_distance, distance)
        
        self.assertAlmostEqual(actual_cost, self.reported_cost, msg="Total travel cost is incorrect.")
        self.assertAlmostEqual(max_distance, self.reported_max_random_spacemax_distance, msg="Maximum distance between consecutive cities is incorrect.")

# Run unit tests
if __name__ == '__main__':
    unittest.main()