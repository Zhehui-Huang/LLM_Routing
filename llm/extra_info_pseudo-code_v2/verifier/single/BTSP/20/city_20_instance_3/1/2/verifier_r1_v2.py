import unittest
import math

class TestOptimizedTour(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
            (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
            (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
            (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
        ]
        self.tour = [0, 1, 10, 11, 4, 7, 14, 8, 18, 12, 0, 3, 15, 17, 16, 9, 5, 19, 6, 13, 2, 0]
        self.reported_cost = 559.53
        self.reported_max_distance = 58.22

    def test_visit_each_city_exactly_once_except_depot(self):
        visited_cities = set(self.tour[1:-1])  # Ignore the first and last indices of the depot
        self.assertEqual(len(visited_cities), len(self.cities) - 1)  # -1 because the depot city is visited twice

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)  # Start at depot
        self.assertEqual(self.tour[-1], 0)  # End at depot

    def test_distance_measurements(self):
        def calc_distance(point1, point2):
            return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

        tour_distances = []
        for i in range(len(self.tour) - 1):
            tour_distances.append(
                calc_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
            )

        total_distance = sum(tour_distances)
        max_distance = max(tour_distances)
        
        # Check if distances match reported distances
        self.assertAlmostEqual(total_distance, self.reported_cost, delta=0.005)
        self.assertAlmostEqual(max_distance, self.reported_max_distance, delta=0.005)

    def test_output_format(self):
        self.assertIsInstance(self.tour, list)
        self.assertIsInstance(self.reported_cost, float)
        self.assertIsInstance(self.reported_max_distance, float)

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)