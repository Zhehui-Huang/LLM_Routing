import unittest
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
            5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
            10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
        }
        
        self.robots = [
            [0, 8, 3, 0],
            [0, 1, 10, 0],
            [0, 6, 7, 2, 0],
            [0, 4, 11, 0],
            [0, 0],
            [0, 5, 14, 0],
            [0, 13, 9, 0],
            [0, 15, 12, 0]
        ]
        
        self.expected_costs = [
            72.81785234728197, 41.77216384800009, 51.60939436573847,
            57.394073777130664, 0.0, 62.44277221633522, 68.39398119181286,
            66.12407122823275
        ]
        self.expected_total_cost = 420.5543089745321

    def test_all_cities_visited_once(self):
        visited = set()
        for tour in self.robots:
            for city in tour:
                if city != 0:  # ignoring the depot start/end repetitions
                    visited.add(city)
        self.assertEqual(len(visited), len(self.cities) - 1)

    def test_start_from_depot_city_zero(self):
        for tour in self.robots:
            self.assertEqual(tour[0], 0)

    def test_total_travel_cost_for_each_tour(self):
        for idx, tour in enumerate(self.robots):
            cost = 0
            for i in range(len(tour) - 1):
                cost += euclidean_distance(self.cities[tour[i]], self.cities[tour[i+1]])
            self.assertAlmostEqual(cost, self.expected_costs[idx], places=5)

    def test_overall_total_travel_cost(self):
        total_cost = sum(self.expected_costs)
        self.assertAlmostEqual(total_cost, self.expected_total_cost, places=5)

def main():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestRobotTours))
    runner = unittest.TextTestRunner()
    results = runner.run(test_suite)
    
    if results.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")
        
if __name__ == "__main__":
    main()