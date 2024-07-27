import unittest
from math import sqrt

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        # Defined city coordinates
        self.city_coordinates = [
            (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
            (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
            (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
            (62, 63), (63, 69), (45, 35)
        ]
        # Solution provided
        self.robot0_tour = [0, 17, 9, 13, 2, 8, 18, 15, 11, 4, 0, 16, 6, 20, 5, 14, 7, 19, 3, 12, 10, 1]
        self.robot1_tour = [1, 1]
        self.robot0_cost = 264.09095230920883
        self.robot1_cost = 0.0
        self.total_cost = 264.09095230920883

    def test_all_cities_visited_once(self):
        combined_tours = self.robot0_tour + self.robot1_tour
        all_cities = list(range(21))  # Cities from 0 to 20
        self.assertCountEqual(combined_tours, all_cities, "Each city must be visited exactly once.")

    def test_tours_start_and_end_with_depot(self):
        self.assertTrue(self.robot0_tour[0] == 0 and self.robot0_tour[-1] == 1, "Robot 0 should start at depot 0 and can end at any depot.")
        self.assertTrue(self.robot1_tour[0] == 1 and self.robot1_tour[-1] == 1, "Robot 1 should start and end at depot 1.")

    def test_calculate_travel_cost(self):
        def calculate_distance(city1, city2):
            x1, y1 = self.city_coordinates[city1]
            x2, y2 = self.city_coordinates[city2]
            return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        # Calculate travel costs based on the tours provided
        calculated_robot0_cost = sum(calculate_distance(self.robot0_tour[i], self.robot0_tour[i+1]) for i in range(len(self.robot0_tour) - 1))
        calculated_robot1_cost = sum(calculate_distance(self.robot1_tour[i], self.robot1_tour[i+1]) for i in range(len(self.robot1_tour) - 1))

        self.assertAlmostEqual(calculated_robot0_cost, self.robot0_cost, places=5, msg="Transport cost for Robot 0 should be accurate.")
        self.assertAlmostEqual(calculated_robot1_cost, self.robot1_cost, places=5, msg="Transport cost for Robot 1 should be accurate.")

    def test_total_transport_cost(self):
        calculated_total_cost = self.robot0_cost + self.robot1_cost
        self.assertAlmostEqual(calculated_total_cost, self.total_cost, places=5, msg="Total transport cost calculation should be accurate.")
    
    def test_output_format(self):
        is_correct_format0 = isinstance(self.robot0_tour, list) and all(isinstance(x, int) for x in self.robot0_tour)
        is_correct_format1 = isinstance(self.robot1_tour, list) and all(isinstance(x, int) for x in self.robot1_tour)
        self.assertTrue(is_correct_format0, "Robot 0's tour should be a list of integers.")
        self.assertTrue(is_correct_format1, "Robot 1's tour should be a list of integers.")

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)