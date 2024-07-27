import unittest
from math import sqrt

def euclidean_distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        self.coordinates = [
            (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
            (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
            (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
            (62, 63), (63, 69), (45, 35)
        ]
        
        self.robot_0_tour = [0, 6, 20, 14, 9, 2, 8, 19, 12, 11, 10, 0]
        self.robot_1_tour = [1, 16, 5, 17, 13, 7, 18, 3, 15, 4, 1]

        self.expected_robot_0_cost = 143.16569415731448
        self.expected_robot_1_cost = 149.60004468688751
        self.expected_total_cost = 292.765738844202

    def test_tour_starts_and_ends_at_depot(self):
        self.assertIs(self.robot_0_tour[0], self.robot_0_tour[-1], "Robot 0 does not start and end at the depot")
        self.assertIs(self.robot_1_tour[0], self.robot_1_tour[-1], "Robot 1 does not start and end at the depot")

    def test_cities_visit_exactly_once(self):
        combined_tours = self.robot_0_tour[:-1] + self.robot_1_tour[:-1]
        all_city_indices = set(range(21))
        self.assertEqual(set(combined_tours), all_city_indices, "Not all cities are visited exactly once")

    def test_calculated_travel_costs(self):
        def calculate_total_tour_cost(tour):
            return sum(euclidean_distance(
                self.coordinates[tour[i]][0], self.coordinates[tour[i]][1],
                self.coordinates[tour[i + 1]][0], self.coordinates[tour[i + 1]][1])
                for i in range(len(tour) - 1))
        
        robot_0_cost = calculate_total_tour_cost(self.robot_0_tour)
        robot_1_cost = calculate_total_tour_cost(self.robot_1_tour)

        self.assertAlmostEqual(robot_0_cost, self.expected_robot_0_cost, places=5, "Robot 0 travel cost mismatch")
        self.assertAlmostEqual(robot_1_cost, self.expected_robot_1_cost, places=5, "Robot 1 travel cost mismatch")
        self.assertAlmostEqual(robot_0_cost + robot_1_cost, self.expected_total_cost, places=5, "Total travel cost mismatch")

if __name__ == '__main__':
    unittest.main()