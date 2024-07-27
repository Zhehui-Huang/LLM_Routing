import unittest
import math

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        # Coordinates of cities
        self.coordinates = {
            0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247),
            6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
            12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193),
            18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
        }
        
        # Tours of each robot
        self.tours = {
            0: [0, 14, 16, 17, 20, 18, 15, 12, 10, 8, 6, 7, 5, 9, 2, 1, 3, 4, 11, 13, 19, 21, 0],
            1: [0, 14, 16, 17, 20, 18, 15, 12, 10, 8, 6, 7, 5, 9, 2, 1, 3, 4, 11, 13, 19, 21, 0],
            2: [0, 14, 16, 17, 20, 18, 15, 12, 10, 8, 6, 7, 5, 9, 2, 1, 3, 4, 11, 13, 19, 21, 0],
            3: [0, 14, 16, 17, 20, 18, 15, 12, 10, 8, 6, 7, 5, 9, 2, 1, 3, 4, 11, 13, 19, 21, 0]
        }
        
        # Expected travel cost for each robot
        self.expected_costs = [312.09, 312.09, 312.09, 312.09]
        
    def test_all_cities_covered_once(self):
        all_cities_visited = set()
        for tour in self.tours.values():
            # Ignore the repeat of the starting depot at the end
            all_cities_visited.update(tour[:-1])
        self.assertEqual(len(all_cities_visited), 22)
    
    def test_tour_starts_and_ends_at_depot(self):
        for robot_id, tour in self.tours.items():
            self.assertEqual(tour[0], 0, f"Robot {robot_id}'s tour does not start at depot city 0")
            self.assertEqual(tour[-1], 0, f"Robot {robot_id}'s tour does not end at depot city 0")
    
    def test_traveldistances(self):
        def calculate_distance(city1, city2):
            return math.sqrt((self.coordinates[city1][0] - self.coordinates[city2][0])**2 + (self.coordinates[city1][1] - self.coordinates[city2][1])**2)
        
        for robot_id, tour in self.tours.items():
            travel_cost = 0
            for i in range(len(tour) - 1):
                travel_cost += calculate_distance(tour[i], tour[i+1])
            # Check if the calculated and expected travel costs are close enough
            self.assertAlmostEqual(travel_cost, self.expected_costs[robot_id], delta=0.1, msg=f"Travel cost for robot {robot_id} does not match expected cost.")

        
if __name__ == "__main__":
    unittest.main()