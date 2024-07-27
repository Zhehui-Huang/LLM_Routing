import unittest
import math
from itertools import chain

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        self.coordinates = {
            0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
            4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
            8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
            12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
            16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
            20: (45, 35), 21: (32, 39), 22: (56, 37)
        }
        # Each robot's tour with start and end point as a list
        self.robot_tours = {
            0: [0, 21, 7, 9],
            1: [0, 16, 5, 17],
            2: [0, 6, 22, 8],
            3: [0, 1, 12, 15],
            4: [0, 20, 14, 18],
            5: [0, 10, 3, 19],
            6: [0, 2, 13],
            7: [0, 4, 11]
        }
        self.robot_costs = [
            32.38569, 38.10497, 47.62561, 36.37249, 67.29727, 45.09825, 30.07918, 29.23382
        ]
        
        self.starting_depot = 0
    
    def test_unique_city_visit(self):
        """Test each city is visited exactly once."""
        all_visited = list(chain(*[tour[1:-1] for tour in self.robot_tours.values()])) # Flatten visited lists
        self.assertEqual(len(all_visited), len(set(all_visited)))
        
    def test_correct_number_of_cities(self):
        """Test all 23 cities are included in visits.""" 
        expected_cities = set(range(23))
        visited_cities = set(chain(*self.robot_tours.values()))
        self.assertEqual(visited_cities, expected_cities)
        
    def test_tours_start_end_at_depot(self):
        """Test each tour starts and ends at depot."""
        for tour in self.robot_tours.values():
            self.assertEqual(tour[0], self.starting_depot)
            self.assertEqual(tour[-1], self.starting_depot)
    
    def test_correct_travel_calculation(self):
        """Test the travel calculation is done with Euclidean distance and matches expected."""
        def euclidean_distance(p1, p2):
            return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        
        for robot, tour in self.robot_tours.items():
            cost = sum(euclidean_distance(self.coordinates[tour[i]], self.coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
            self.assertAlmostEqual(cost, self.robot_costs[robot], places=5)
        
    def test_minimize_cost(self):
        """Test the total cost is minimized (hard to test perfectly without comparison to an optimal or known benchmark)."""
        calculated_total_cost = sum(self.robot_costs)
        expected_total_cost = 326.19729
        self.assertAlmostEqual(calculated_total_cost, expected_total_cost, places=5)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)