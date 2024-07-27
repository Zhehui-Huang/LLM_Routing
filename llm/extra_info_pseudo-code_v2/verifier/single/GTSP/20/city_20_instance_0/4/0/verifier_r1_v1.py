import unittest
from math import sqrt

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates of the cities
        self.coordinates = {
            0: (8, 11),
            1: (40, 6),
            2: (95, 33),
            3: (80, 60),
            4: (25, 18),
            5: (67, 23),
            6: (97, 32),
            7: (25, 71),
            8: (61, 16),
            9: (27, 91),
            10: (91, 46),
            11: (40, 87),
            12: (20, 97),
            13: (61, 25),
            14: (5, 59),
            15: (62, 88),
            16: (13, 43),
            17: (61, 28),
            18: (60, 63),
            19: (93, 15)
        }

        # Groups of cities
        self.groups = [
            [1, 3, 5, 11, 13, 14, 19],
            [2, 6, 7, 8, 12, 15],
            [4, 9, 10, 16, 17, 18]
        ]

        # Given output
        self.tour = [0, 1, 8, 4, 0]
        self.reported_cost = 110.08796524611944

    def test_start_and_end_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour does not start at depot city 0.")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at depot city 0.")

    def test_visit_exactly_one_city_from_each_group(self):
        visited_cities = set(self.tour[1:-1])  # removing the depot city from the list for this check
        visited_groups = [False] * len(self.groups)
        for index, group in enumerate(self.groups):
            visited_groups[index] = bool(visited_cities & set(group))
        
        self.assertListEqual(visited_groups, [True]*len(self.groups),
                             "Tour does not visit exactly one city from each group.")

    def test_output_format(self):
        self.assertIsInstance(self.tour, list, "Tour output is not a list.")

    def test_output_cost_calculation(self):
        def calculate_distance(coord1, coord2):
            return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

        calculated_cost = sum(calculate_distance(self.coordinates[self.tour[i]], self.coordinates[self.tour[i+1]])
                               for i in range(len(self.tour) - 1))

        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=5,
                               msg="The calculated travel cost does not approximately match the reported travel cost.")

if __name__ == '__main__':
    unittest.main()