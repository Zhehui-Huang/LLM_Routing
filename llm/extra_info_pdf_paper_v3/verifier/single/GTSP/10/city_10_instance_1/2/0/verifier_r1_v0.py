import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        # City coordinates
        self.cities = {
            0: (53, 68),
            1: (75, 11),
            2: (91, 95),
            3: (22, 80),
            4: (18, 63),
            5: (54, 91),
            6: (70, 14),
            7: (97, 44),
            8: (17, 69),
            9: (95, 89)
        }
        # Groups of cities
        self.groups = [
            [5, 6, 7],
            [2, 3],
            [1, 9],
            [4, 8]
        ]
        # Provided tour solution
        self.tour = [0, 5, 2, 9, 8, 0]
        self.reported_cost = 183.99

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour does not start at depot")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at depot")

    def test_tour_includes_one_city_from_each_group(self):
        visited_groups = set()
        for city in self.tour[1:-1]:  # exclude the starting and ending depot city
            for index, group in enumerate(self.groups):
                if city in group:
                    visited_groups.add(index)
        self.assertEqual(len(visited_groups), 4, "Tour does not visit exactly one city from each group")

    def test_travel_cost(self):
        total_distance = 0
        for i in range(len(self.tour) - 1):
            total_distance += calculate_distance(self.cities[self.tour[i]], self.cities[self.tour[i+1]])
        self.assertAlmostEqual(total_distance, self.reported_cost, places=2, msg="Total travel cost is incorrect")

    def test_output_format(self):
        self.assertIsInstance(self.tour, list, "Tour output should be a list")
        self.assertIsInstance(self.reported_cost, float, "Cost should be a float")

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)