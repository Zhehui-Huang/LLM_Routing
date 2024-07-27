import math
import unittest

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        # Coordinates for each city
        self.coordinates = {
            0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
            5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
            10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27),
            14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
        }
        # Tour for robot 0 corrected
        self.robot_0_tour = [0, 2, 11, 4, 3, 12, 8, 16, 17, 14, 10, 9, 15, 5, 7, 6, 18, 13, 0]
        # Expected total cost for the tour
        self.expected_cost = 273.03

    def test_tour_starts_and_ends_at_depot(self):
        """ Test if the tour starts and ends at the designated depot."""
        self.assertEqual(self.robot_0_tour[0], 0, "Tour should start at depot 0")
        self.assertEqual(self.robot_0_tour[-1], 0, "Tour should end at depot 0")

    def test_visit_each_city_exactly_once(self):
        """ Test if each city is visited exactly once, excluding the depots. """
        cities_visited = self.robot_0_tour[1:-1]  # Exclude the start/end depot
        unique_cities = set(cities_visited)
        self.assertEqual(len(cities_visited), len(unique_cities), "Each city should be visited exactly once")

    def test_all_cities_included(self):
        """ Test if all cities are included in the tour. """
        cities_visited = set(self.robot_0_tour)  # Include depots
        all_cities = set(range(19))  # All cities from 0 to 18
        self.assertEqual(cities_visited, all_cities, "Tour should include all cities")
    
    def test_calculate_total_travel_cost(self):
        """ Calculate and verify the total travel cost is as expected. """
        total_cost = 0
        for i in range(len(self.robot_0_tour) - 1):
            start = self.robot_0_tour[i]
            end = self.robot_0_tour[i + 1]
            dx = self.coordinates[start][0] - self.coordinates[end][0]
            dy = self.coordinates[start][1] - self.coordinates[end][1]
            dist = math.hypot(dx, dy)
            total_cost += dist
        self.assertAlmostEqual(total_cost, self.expected_cost, places=2, msg="Total travel cost should be close to the expected cost")

if __name__ == '__main__':
    unittest.main()