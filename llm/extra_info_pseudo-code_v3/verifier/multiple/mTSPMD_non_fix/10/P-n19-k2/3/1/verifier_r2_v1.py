import unittest
import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        # Coordinates of all cities including depots
        self.city_coords = {
            0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
            5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
            10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
            15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
        }

        # Tours and costs
        self.robot_0_tour = [0, 2, 9, 15, 8, 16, 17, 12, 14, 0]
        self.robot_1_tour = [1, 10, 4, 11, 3, 7, 5, 18, 6, 13, 1]
        self.robot_0_cost = 136.05815649765321
        self.robot_1_cost = 150.58145502061055
        self.overall_cost = 286.6396115182638

    def test_no_duplicate_cities_in_each_tour(self):
        # Check that all cities are visited exactly once between the robots
        combined_tours = self.robot_0_tour + self.robot_1_tour
        self.assertEqual(len(combined_tours), len(set(combined_tours)))

    def test_calculate_tour_cost(self):
        # Helper function to sum up distance costs in a tour
        def tour_cost(tour):
            return sum(calculate_euclidean_distance(
                self.city_coords[tour[i]][0], self.city_coords[tour[i]][1],
                self.city_coords[tour[i + 1]][0], self.city_coords[tour[i + 1]][1]
            ) for i in range(len(tour) - 1))

        total_cost_calculated_0 = tour_cost(self.robot_0_tour)
        total_cost_calculated_1 = tour_cost(self.robot_1_tour)
        
        self.assertAlmostEqual(total_cost_calculated_0, self.robot_0_cost)
        self.assertAlmostEqual(total_cost_calculated_1, self.robot_1_cost)

    def test_correct_start_and_end(self):
        # Ensure each route starts and ends at the correct depots and not return mandatory
        self.assertEqual(self.robot_0_tour[0], 0) # Start at depot 0
        self.assertIn(self.robot_0_tour[-1], [0]) # Acceptable to end at depot 0
        self.assertEqual(self.robot_1_tour[0], 1) # Start at depot 1
        self.assertIn(self.robot_1_tour[-1], [1]) # Acceptable to end at depot 1

    def test_total_cost(self):
        # Ensure the overall cost is correctly calculated
        self.assertAlmostEqual(
            self.robot_0_cost + self.robot_1_cost,
            self.overall_cost
        )

if __name__ == '__main__':
    unittest.main()