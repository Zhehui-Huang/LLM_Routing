import unittest
import math

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        # City coordinates as provided
        self.cities = {
            0: (30, 40),
            1: (37, 52),
            2: (49, 49),
            3: (52, 64),
            4: (31, 62),
            5: (52, 33),
            6: (42, 41),
            7: (52, 41),
            8: (57, 58),
            9: (62, 42),
            10: (42, 57),
            11: (27, 68),
            12: (43, 67),
            13: (58, 48),
            14: (58, 27),
            15: (37, 69),
            16: (38, 46),
            17: (61, 33),
            18: (62, 63),
            19: (63, 69),
            20: (45, 35)
        }
        # Simulated solution
        self.robot_0_tour = [0, 2, 3, 0]
        self.robot_1_tour = [1, 4, 5, 1]
        self.robot_0_cost = self.calculate_total_travel_cost(self.robot_0_tour)
        self.robot_1_cost = self.calculate_total_travel_cost(self.robot_1_tour)
        self.total_cost = self.robot_0_cost + self.robot_1_cost

    def calculate_distance(self, city1, city2):
        """Calculate Euclidean distance between two cities."""
        return math.sqrt((self.cities[city1][0] - self.cities[city2][0]) ** 2 + 
                         (self.cities[city1][1] - self.cities[city2][1]) ** 2)
    
    def calculate_total_travel_cost(self, tour):
        """Calculate the total travel cost of a given tour."""
        total_cost = 0
        for i in range(1, len(tour)):
            total_cost += self.calculate_distance(tour[i-1], tour[i])
        return total_cost
    
    def test_tour_starts_ends_at_depot(self):
        """Test that each robot's tour starts and ends at the assigned depot."""
        self.assertEqual(self.robot_0_tour[0], self.robot_0_tour[-1], "Robot 0's tour does not start and end at the same depot")
        self.assertEqual(self.robot_1_tour[0], self.robot_1_tour[-1], "Robot 1's tour does not start and end at the same depot")

    def test_total_number_of_cities_visited_once(self):
        """Test that all cities are visited exactly once across all tours."""
        combined_tours = self.robot_0_tour[:-1] + self.robot_1_tour[:-1]  # Exclude the repeated depot city at the ends
        unique_cities_visited = set(combined_tours)
        self.assertEqual(len(unique_cities_visited), 21, "Not all 21 cities are visited exactly once")

    def test_correct_total_cost(self):
        """Test the correctness of total cost calculations."""
        expected_robot_0_cost = 174.65889255351078
        expected_robot_1_cost = 174.6977835794075
        expected_total_cost = 349.3566761329183
        
        self.assertAlmostEqual(self.robot_0_cost, expected_robot_0_cost, places=5, msg="Robot 0 tour cost is incorrect")
        self.assertAlmostEqual(self.robot_1_cost, expected_robot_1_cost, places=5, msg="Robot 1 tour cost is incorrect")
        self.assertAlmostEqual(self.total_cost, expected_total_cost, places=5, msg="Overall total tour cost is incorrect")

    def test_tour_minimization_goal(self):
        """Verify if the tours are optimized for the least distance or not.
        This is indicative and should thoroughly be tested with known optimal solutions or bounds."""
        known_optimal_bound = 349.356  # Hypothetical optimal known from an efficient solution for easy comparison
        self.assertTrue(self.total_opt <= known_optimal_bound, "Tours do not minimize the total distance adequately")

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)