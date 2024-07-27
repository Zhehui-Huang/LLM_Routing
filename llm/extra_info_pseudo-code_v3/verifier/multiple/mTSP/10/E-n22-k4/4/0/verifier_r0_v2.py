import unittest
import math

class RobotTourTestCase(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
            5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
            10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
            15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
            20: (155, 185), 21: (139, 182)
        }
        
        self.robot_tours = {
            0: [0, 13, 17, 21, 9, 5, 1, 0],
            1: [0, 14, 18, 10, 6, 2, 0],
            2: [0, 15, 7, 3, 11, 19, 0],
            3: [0, 16, 12, 8, 4, 20, 0]
        }
        
        # each robot's calculated distance 
        self.expected_costs = {
            0: 197.5591024687469,
            1: 154.7311246419968,
            2: 183.24946422163586,
            3: 177.4902176700044
        }

    def test_all_cities_visited_once(self):
        visited_cities = set()
        for tour in self.robot_tours.values():
            for city in tour[1:-1]:  # exclude the depot (first and last)
                if city in visited_cities:
                    self.fail("City {} visited more than once.".format(city))
                visited_cities.add(city)
        self.assertEqual(len(visited_cities), len(self.cities)-1)  # excluding depot
    
    def test_total_travel_cost(self):
        overall_cost_computed = 0
        for robot_id, tour in self.robot_tours.items():
            cost = 0
            for i in range(len(tour)-1):
                city_a, city_b = self.cities[tour[i]], self.cities[tour[i+1]]
                cost += math.hypof(city_b[0] - city_a[0], city_b[1] - city_a[1])
            overall_cost_computed += cost
            self.assertAlmostEqual(cost, self.expected_costs[robot_id], places=5)
        self.assertAlmostEqual(overall_cost_computed, sum(self.expected_costs.values()), places=5)

    def test_each_tour_starts_and_ends_at_depot(self):
        for tour in self.robot_tours.values():
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(RobotTourTestCase)
    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

run_tests()