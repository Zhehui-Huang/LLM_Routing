import unittest
from math import sqrt

# Coordinates of cities
city_coordinates = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 20),
    13: (26, 29),
    14: (21, 79),
    15: (50, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# City groups
city_groups = {
    0: [5, 6, 7, 11, 17],
    1: [1, 4, 8, 13, 16],
    2: [2, 10, 15, 18, 19],
    3: [3, 9, 12, 14]
}

class TestTourSolution(unittest.TestCase):
    def test_environment_city_count(self):
        self.assertEqual(len(city_coordinates), 20)

    def test_depot_city(self):
        depot_coord = city_coordinates[0]
        self.assertEqual(depot_coord, (14, 77))

    def test_city_groups(self):
        all_cities_from_groups = sum(city_groups.values(), [])
        unique_cities = set(all_cities_from_groups)
        self.assertEqual(len(all_cities_from_groups), len(unique_cities))

    def test_visit_one_city_per_group(self):
        tour = [0, 6, 13, 2, 9, 0]
        visited_groups = []
        for city in tour:
            for group_id, cities in city_groups.items():
                if city in cities:
                    visited_groups.append(group_id)
        unique_groups_visited = set(visited_groups)
        self.assertEqual(len(unique_groups_visited), 4)

    def test_return_to_depot(self):
        tour = [0, 6, 13, 2, 9, 0]
        self.assertEqual(tour[0], tour[-1])

    def test_tour_format(self):
        tour = [0, 6, 13, 2, 9, 0]
        self.assertIsInstance(tour, list)

    def test_distance_calculation(self):
        tour = [0, 6, 13, 2, 9, 0]
        computed_distance = 0
        for i in range(len(tour) - 1):
            (x1, y1), (x2, y22) = city_coordinates[tour[i]], city_coordinates[tour[i + 1]]
            computed_distance += sqrt((x2 - x1) ** 2 + (y22 - y1) ** 2)
        expected_distance = 114.65928837582914
        self.assertAlmostEqual(computed_distance, expected_distance, places=5)

    def test_solution_correctness(self):
        self.test_environment_city_counts()
        self.test_depot_city()
        self.test_city_groups()
        self.test_visit_one_city_per_group()
        self.test_return_to_deptot()
        self.test_tour_format()
        self.test_distance_calculation()
        print("CORRECT")

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)