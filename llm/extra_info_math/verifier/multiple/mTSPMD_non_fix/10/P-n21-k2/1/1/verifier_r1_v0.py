import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
            5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
            10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
            15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
            20: (45, 35)
        }
        self.robot_0_tour = [0, 0]
        self.robot_1_tour = [1, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.total_cost = 0  # As per provided solution, though it is likely incorrect.
    
    def test_starts_from_depot(self):
        self.assertEqual(self.robot_0_tour[0], 0)
        self.assertEqual(self.robot_1_tour[0], 1)
    
    def test_each_city_visited_once(self):
        all_cities_visited = sorted(self.robot_0_tour + self.robot_1_tour[1:])  # Avoid counting depot 1 twice
        expected_cities = list(range(21))
        self.assertEqual(all_cities_visited, expected_cities)
    
    def test_ends_at_any_city(self):
        last_city_robot_0 = self.robot_0_tour[-1]
        last_city_robot_1 = self.robot_1_tour[-1]
        self.assertNotEqual(last_city_robot_0, 0)  # Ends at different city
        self.assertNotEqual(last_city_robot_1, 1)  # Ends at different city
    
    def test_minimized_travel_cost(self):
        # This function computes the Euclidean distance between cities
        def distance(city1, city2):
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        # Sum up the distances of the tours
        cost_robot_0 = sum(distance(self.robot_0_tour[i], self.robot_0_tour[i + 1]) for i in range(len(self.robot_0_tour) - 1))
        cost_robot_1 = sum(distance(self.robot_1_tour[i], self.robot_1_tour[i + 1]) for i in range(len(self.robot_1_tour) - 1))
        self.assertEqual(cost_robot_0 + cost_robot_1, self.total_cost)
    
    def test_no_city_visited_more_than_once(self):
        # Combine and check if any city is visited more than once
        all_visit_counts = {}
        full_tour = self.robot_0_tour + self.robot_1_tour
        for city in full_tour:
            if city in all_visit_counts:
                all_visit_counts[city] += 1
            else:
                all_visit_counts[city] = 1
        self.assertTrue(all(count==1 for city, count in all_visit_cs.iteritems() if city not in {0, 1}))
        

if __name__ == "__main__":
    unittest.main()