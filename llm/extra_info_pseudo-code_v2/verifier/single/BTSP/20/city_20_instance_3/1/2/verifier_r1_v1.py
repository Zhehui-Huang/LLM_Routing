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
        self.reported_tour = [0, 1, 10, 11, 4, 7, 14, 8, 18, 12, 0, 3, 15, 17, 16, 9, 5, 19, 6, 13, 2, 0]
        self.reported_cost = 559.53
        self.reported_max_distance = 58.22

    def test_visit_each_city_exactly_once(self):
        # Count visits for each city index, excluding the repeat visit to the depot (at start and end)
        city_visit_count = [0] * len(self.cities)
        for city_index in self.reported_tour:
            city_visit_count[city_index] += 1

        # Depot visited 3 times, others should be visited exactly once
        self.assertEqual(city_visit_count[0], 3)
        for count in city_visit_data[1:]:
            self.assertEqual(count, 1)

    def test_euclidean_distances(self):
        def calc_distance(city1, city2):
            return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
        
        # Calculate total distance and max distance
        total_distance = 0
        max_distance = 0
        for i in range(1, len(self.reported_tour)):
            distance = calc_distance(self.cities[self.reported_tour[i-1]], self.cities[self.reported_tour[i]])
            total_distance += distance
            if distance > max_distance:
                max_distance = distance
        
        # Assert that the calculated and reported values match
        self.assertAlmostEqual(total_distance, self.reported_cost, places=2)
        self.assertAlmostEqual(max_distance, self.reported_max_distance, places=2)

    def test_output_format(self):
        self.assertIsInstance(self.reported_tour, list)  # tour is a list
        self.assertTrue(all(isinstance(x, int) for x in self.reported_tour))  # all elements in tour are ints
        self.assertIsInstance(self.reported_cost, float)  # cost is a float
        self.assertIsInstance(self.reported_max_distance, float)  # max distance is a float

if __name__ == '__main__':
    unittest.main()