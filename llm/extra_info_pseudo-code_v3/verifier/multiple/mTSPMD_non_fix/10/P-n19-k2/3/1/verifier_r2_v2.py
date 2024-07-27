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
        # This test ensures all cities are visited exactly once by removing duplicates of the depot
        # Remove last city as it is the depot where the tour ends
        unique_cities_robot_0 = set(self.robot_0_tour[:-1])
        unique_cities_robot_1 = set(self.robot_1_tour[:-1])
        combined_unique_cities = unique_cities_robot_0.union(unique_cities_robot_1)
        self.assertEqual(len(combined_unique_cities), 18)  # Expect 18 unique cities excluding the depot

    def test_correct_tour_length(self):
        # Test the cumulative distances against provided distances
        def calculate_total_tour_cost(tour):
            total_cost = 0
            for i in range(len(tour) - 1):
                city_a = tour[i]
                city_b = tour[i + 1]
                total_cost += calculate_euclidean_distance(
                    *self.city_coords[city_a], *self.city_coords[city_b])
            return total_cost

        calculated_cost_0 = calculate_total_tour_cost(self.robot_0_tour)
        calculated_cost_1 = calculate_total_tour_cost(self.robot_1_tour)

        self.assertAlmostEqual(calculated_cost_0, self.robot_0_cost)
        self.assertAlmostEqual(calculated_cost_1, self.robot_1_cost)

    def test_correct_starts_and_ends(self):
        # Check if each robot starts and ends at the correct depots
        self.assertEqual(self.robot_0_tour[0], self.robot_0_tour[-1])
        self.assertEqual(self.robot_0_tour[0], 0)  # Starts and ends at depot 0
        self.assertEqual(self.robot_1_tour[0], self.robot_1_tour[-1])
        self.assertEqual(self.robot_1_tour[0], 1)  # Starts and ends at depot 1

    def test_total_cost_accuracy(self):
        # Total combined cost must match expected total cost
        total_cost_calculated = self.robot_0_cost + self.robot_1_cost
        self.assertAlmostEqual(total_cost_calculated, self.overall_cost)

if __name__ == '__main__':
    unittest.main()