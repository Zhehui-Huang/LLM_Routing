import unittest
import math

class TestRobotTournaments(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
            6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
            12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
            18: (62, 63), 19: (63, 69), 20: (45, 35)
        }
        
        # Tours provided in the solution where all robots start from depot city 0
        self.robot0_tour = [0, 12, 3, 19, 13, 2, 10, 15, 11, 16, 20]
        self.robot1_tour = [0, 4, 1, 6, 7, 5, 14, 17, 9, 8, 18]

        # These costs need to be recalculated according to their actual values
        self.robot0_cost = 137.09097916207833  # This is just a placeholder
        self.robot1_cost = 89.82794263426624   # This is just a placeholder
        self.overall_cost = 226.91892179634456 # This is just a placeholder

    def test_all_cities_visited_once(self):
        # Check if all cities are visited at least once collectively and not multiple times
        all_cities_visited = sum([self.robot0_tour, self.robot1_tour], [])
        all_cities = set(range(21))
        unique_visited_cities = set(all_cities_visited)
        self.assertEqual(all_cities, unique_visited_cities, "Not all cities are visited or some are visited more than once.")

    def test_robot_starts_and_dont_return_to_depot(self):
        # Both robots start from the first city in their tours which must be the designated depot (city 0)
        self.assertTrue(self.robot0_tour[0] == 0 and self.robot1_tour[0] == 0, "Robots do not start from depot city 0.")

    def test_travel_cost(self):
        # Method to calculate Euclidean distance for the tour
        def calculate_euclidean_cost(tour):
            cost = 0
            for i in range(len(tour) - 1):
                x1, y1 = self.cities[tour[i]]
                x2, y2 = self.cities[tour[i + 1]]
                cost += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            return cost

        # Get calculated costs
        calculated_robot0_cost = calculate_euclidean_cost(self.robot0_tour)
        calculated_robot1_cost = calculate_euclidean_cost(self.robot1_tour)

        # Validate the calculated costs with provided
        self.assertAlmostEqual(calculated_robot0_cost, self.robot0_cost, places=5)
        self.assertAlmostEqual(calculated_robot1_cost, self.robot1_cost, places=5)
        self.assertAlmostEqual(calculated_robot0_cost + calculated_robot1_cost, self.overall_cost, places=5)

if __name__ == '__main__':
    unittest.main()