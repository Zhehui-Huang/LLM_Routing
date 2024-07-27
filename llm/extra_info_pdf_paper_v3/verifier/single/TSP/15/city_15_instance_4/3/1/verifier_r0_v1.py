import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = [
            (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
            (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
            (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
        ]
        self.tour = [0, 1, 5, 9, 2, 7, 10, 8, 3, 6, 14, 13, 11, 12, 4, 0]
        self.reported_cost = 413.62

    def test_tour_contains_all_cities_once(self):
        # Test all cities are present exactly once, except depot which should be present twice
        visits = {city_idx: 0 for city_idx in range(len(self.coordinates))}
        
        for city_idx in self.tour:
            visits[city_idx] += 1

        expected_visits = {0: 2}
        for i in range(1, 15):
            expected_visits[i] = 1
        
        self.assertEqual(visits, expected_visits)

    def test_tour_starts_and_ends_at_depot(self):
        # Test that the tour starts and ends at the depot
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_travel_cost_calculation(self):
        # Test the calculated travel cost matches the given cost
        def euclidean_distance(point1, point2):
            return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

        total_cost = 0
        for i in range(len(self.tour) - 1):
            total_cost += euclidean_errors(self.coordinates[self.tour[i]], self.coordinates[self.tour[i + 1]])
            
        self.assertAlmostEqual(total_cost, self.reported_cost, places=2)

# Run the tests
if __name__ == '__main__':
    unittest.main()