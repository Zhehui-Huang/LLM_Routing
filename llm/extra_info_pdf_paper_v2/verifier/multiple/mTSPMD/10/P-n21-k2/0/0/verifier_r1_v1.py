import unittest
from math import sqrt

class TestRobotTours(unittest.TestCase):
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
        6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
        12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
        18: (62, 63), 19: (63, 69), 20: (45, 35)
    }

    robot0_tour = [0, 2, 12, 11, 4, 15, 3, 18, 8, 20, 16, 0]
    robot1_tour = [1, 10, 19, 9, 6, 7, 5, 13, 14, 17, 1]
    
    def calculate_distance(self, city1, city2):
        x1, y1 = self.cities[city1]
        x2, y2 = self.cities[city2]
        return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
    def test_tours_start_end_at_depot(self):
        self.assertEqual(self.robot0_tour[0], self.robot0_tour[-1])
        self.assertEqual(self.robot0_tour[0], 0)
        self.assertEqual(self.robot1_tour[0], self.robot1_tour[-1])
        self.assertEqual(self.robot1_tour[0], 1)

    def test_city_visitation_exclusivity(self):
        all_visits = self.robot0_tour + self.robot1_tour
        unique_visits = set(all_visits)
        self.assertEqual(len(all_visits) - all_visits.count(0) - all_visits.count(1), len(unique_visits) - 2)
        
    def test_each_city_visited_once(self):
        visited_cities = set(self.robot0_tour[1:-1] + self.robot1_tour[1:-1])
        self.assertSetEqual(visited_cities, set(self.cities.keys()) - {0, 1})

    def test_total_travel_cost(self):
        cost_robot0 = sum(self.calculate_distance(self.robot0_tour[i], self.robot0_tour[i+1]) for i in range(len(self.robot0_tour) - 1))
        cost_robot1 = sum(self.calculate_distance(self.robot1_tour[i], self.robot1_tour[i+1]) for i in range(len(self.robot1_tour) - 1))
        total_cost = cost_robot0 + cost_robot1
        
        self.assertAlmostEqual(cost_robot0, 154.37, places=2)
        self.assertAlmostEqual(cost_robot1, 170.78, places=2)
        self.assertAlmostEqual(total_cost, 325.15, places=2)

if __name__ == '__main__':
    unittest.main()