import unittest
import math

class TestTravelingSalesmanSolution(unittest.TestCase):
    def setUp(self):
        # Given cities with coordinates
        self.cities = {
            0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
            5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
            10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
            15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
            20: (45, 35), 21: (32, 39), 22: (56, 37)
        }
        # Best tour by GA for the robot with starting and potential ending at city 0.
        self.tour = [0, 16, 1, 10, 2, 9, 6, 13, 14, 17, 20, 18, 19, 12, 15, 3, 4, 11, 7, 8, 21, 5, 22]
        # Reported total cost of the tour
        self.reported_cost = 346.0500480846498

    def test_visits_all_cities_exactly_once(self):
        # Check if there are 23 unique visits, ensuring all cities are visited once
        unique_cities_visited = set(self.tour)
        expected_cities = set(range(23))
        self.assertEqual(unique_cities_visited, expected_cities, "All cities must be visited exactly once.")

    def test_final_position_is_any_city(self):
        # The robot can end at any city
        self.assertIn(self.tour[-1], self.cities.keys(), "Final position must be among the city indices")

    def test_minimum_total_travel_cost(self):
        # Calculate the total travel cost based on the Euclidean distance
        def euclidean_distance(city1, city2):
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        total_cost = sum(euclidean_distance(self.tour[i], self.tour[i + 1]) for i in range(len(self.tour) - 1))
        # Compare calculated cost to the reported cost within a slim margin for floating-point arithmetic variability
        self.assertAlmostEqual(total_cost, self.reported_cost, places=5, msg="Calculated cost should be close to the reported one")

    def test_no_city_visited_twice_except_start(self):
        # Ensuring no city but the starting city is visited more than once
        starting_city = self.tour[0]
        tour_without_start = self.tour[1:]
        self.assertTrue(all(tour_without_start.count(city) == 1 for city in tour_without_start))
        self.assertEqual(self.tour.count(starting_city), 1, "Starting city should not be repeated in the tour")

if __name__ == '__main__':
    unittest.main()