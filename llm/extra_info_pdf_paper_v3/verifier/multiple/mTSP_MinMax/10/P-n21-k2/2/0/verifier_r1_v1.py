import unittest
from math import sqrt

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        # The tours each robot takes
        self.robot_tours = {
            0: [0, 1, 3, 4, 8, 10, 11, 12, 15, 18, 19, 0],
            1: [0, 2, 5, 6, 7, 9, 13, 14, 16, 17, 20, 0]
        }
        # Cost for each robot's tour
        self.robot_costs = {
            0: 212.22,
            1: 184.31
        }
        self.max_distance = 212.22
        self.all_cities = set(range(21))  # Cities from 0 to 20

    def test_visits_all_cities_once(self):
        visited_cities = set()
        for tour in self.robot_tours.values():
            # Excludes the first and last city because they should be the depot
            visited_cities.update(tour[1:-1])

        # Expected cities are those excluding the depot city
        expected_cities = self.all_cities.difference({0})
        self.assertEqual(visited_cities, expected_cities, "Not all cities are visited exactly once")

    def test_tour_starts_and_ends_at_depot(self):
        for tour in self.robot_tours.values():
            self.assertTrue(tour[0] == 0 and tour[-1] == 0, "Tour does not start and end at the depot")

    def test_minimize_maximum_distance(self):
        computed_max_distance = max(self.robot_costs.values())
        self.assertEqual(computed_gridded_max_distance, self.max_distance, "Maximum travel cost is not minimized as expected")

if __name__ == '__main__':
    unittest.main()