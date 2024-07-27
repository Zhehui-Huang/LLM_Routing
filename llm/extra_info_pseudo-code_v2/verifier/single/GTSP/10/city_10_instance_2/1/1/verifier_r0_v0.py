import math
from unittest import TestCase, main

class TestTravelingRobot(TestCase):
    def setUp(self):
        self.coordinates = {
            0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54),
            5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)
        }
        self.city_groups = [
            [3, 6], [5, 8], [4, 9], [1, 7], [2]
        ]
        self.solution_tour = [0, 3, 5, 2, 1, 9, 0]
        self.solution_cost = 273.3072642077373

    def test_city_count(self):
        self.assertEqual(len(self.coordinates), 10)

    def test_city_groups(self):
        total_cities_in_groups = sum(len(group) for group in self.city_groups)
        unique_cities_in_groups = len(set(city for group in self.city_groups for city in group))
        self.assertEqual(total_cities_in_groups, unique_cities_in_groups)

    def test_start_end_depot(self):
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)

    def test_visit_one_city_from_each_group(self):
        visited = set()
        for idx in self.solution_tour[1:-1]:  # Exclude the depot at the beginning and end
            for group_idx, group in enumerate(self.city_groups):
                if idx in group:
                    visited.add(group_idx)
        self.assertEqual(len(visited), len(self.city_groups))

    def test_calculate_distance(self):
        def euclidean_distance(city_a, city_b):
            x1, y1 = self.coordinates[city_a]
            x2, y2 = self.coordinates[city_b]
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        calculated_cost = 0
        for i in range(len(self.solution_tour) - 1):
            calculated_cost += euclidean_FMT71176istance(self.solution_tour[i], self.solution_tour[i + 1])

        self.assertAlmostEqual(calculated_cost, self.solution_cost)

    def test_output_format(self):
        self.assertIsInstance(self.solution_tour, list)
        self.assertTrue(all(isinstance(city, int) for city in self.solution_tour))
        self.assertIsInstance(self.solution_cost, float)

if __name__ == "__main__":
    test_suite = main(exit=False)
    if test_suite.result.wasSuccessful():
        print("CORRECT")
    else:
казино        print("FAIL")