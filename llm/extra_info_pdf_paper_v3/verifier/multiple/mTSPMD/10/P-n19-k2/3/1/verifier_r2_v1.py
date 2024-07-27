import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestTSPSolution(unittest.TestCase):
    
    def setUp(self):
        self.cities = {
            0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
            5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
            10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
            15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
        }
        # Provided solution:
        self.robot0_tour = [0, 4, 11, 14, 12, 10, 3, 17, 16, 8, 2, 7, 9, 15, 13, 5, 18, 6, 0]
        self.robot0_cost = 174.03576233257616
    
    def test_robot_tours_start_and_end_at_depot(self):
        # Requirement 2: Start and end at a depot
        self.assertEqual(self.robot0_tour[0], self.robot0_tour[-1])
        self.assertEqual(self.robot0_tour[0], 0)  # Depot 0

    def test_all_cities_visited_exactly_once(self):
        # Requirement 1: All cities visited exactly once (besides depot repeated at end)
        visited_cities = set(self.robot0_tour[1:-1])  # Exclude the depot occurrences
        self.assertSetEqual(visited_cities, set(range(2, 19)))  # Cities 2-18 should be visited
        
    def test_total_travel_cost_is_accurate(self):
        # Requirement 4: Calculate travel costs using Euclidean distance
        total_cost = 0
        for i in range(len(self.robot0_tour) - 1):
            city1 = self.robot0_tour[i]
            city2 = self.robot0_tour[i + 1]
            total_cost += calculate_distance(self.cities[city1], self.cities[city2])
        self.assertAlmostEqual(total_cost, self.robot0_cost, places=5)

def main():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestTSPSolution))
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

if __name__ == "__main__":
    main()