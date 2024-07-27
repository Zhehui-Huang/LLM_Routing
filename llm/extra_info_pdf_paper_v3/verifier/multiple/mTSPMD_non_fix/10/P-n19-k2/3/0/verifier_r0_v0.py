import unittest
from math import sqrt

class TestRobotTourSolution(unittest.TestCase):
    def setUp(self):
        # City coordinates with depot being 0 and 1
        self.city_coords = {
            0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
            5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
            10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
            15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
        }
        
        # Tours given in the solution
        self.robot_0_tour = [0, 6, 7, 16, 3, 12, 14, 11, 4, 0]
        self.robot_1_tour = [1, 5, 13, 18, 2, 15, 9, 8, 17, 10, 1]
        
        # Provided costs
        self.robot_0_cost = 111.35264416553834
        self.robot_1_cost = 142.1280719276256
        self.total_cost = 253.48071609316395
    
    def calculate_distance(self, city1, city2):
        x1, y1 = self.city_coords[city1]
        x2, y2 = self.city_coords[city2]
        return sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def test_starts_from_depot(self):
        self.assertEqual(self.robot_0_tour[0], 0)
        self.assertEqual(self.robot_1_tour[0], 1)
    
    def test_does_not_return_to_depot(self):
        # Since they may end at any city, check last city
        self.assertNotEqual(self.robot_0_tour[-1], self.robot_0_tour[0])
        self.assertNotEqual(self.robot_1_tour[-1], self.robot_1_tour[0])

    def test_visit_all_cities_once(self):
        all_cities_visited = set(self.robot_0_tour + self.robot_1_tour)
        self.assertSetEqual(all_cities_visited, set(range(19)))  # 19 cities, 0-18
    
    def test_costs(self):
        # Calculate tour costs
        robot_0_calculated_cost = sum(self.calculate_distance(self.robot_0_tour[i], self.robot_0_tour[i+1]) 
                                      for i in range(len(self.robot_0_tour)-1))
        robot_1_calculated_cost = sum(self.calculate_distance(self.robot_1_tour[i], self.robot_1_tour[i+1]) 
                                      for i in range(len(self.robot_1_tour)-1))

        # Check each cost with a certain tolerance
        self.assertAlmostEqual(robot_0_calculated_cost, self.robot_0_cost, places=4)
        self.assertAlmostEqual(robot_1_calculated_cost, self.robot_1_cost, places=4)
        self.assertAlmostEqual(robot_0_calculated_cost + robot_1_calculated_cost, self.total_cost, places=4)

    def test_each_city_visited_once_by_any_robot(self):
        unique_cities = self.robot_0_tour[:-1] + self.robot_1_tour[:-1]  # exclude repetition of start city at end
        self.assertEqual(len(unique_cities), len(set(unique_cities)))

# Run tests
if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTourSolution)
    test_result = unittest.TextTestRunner(verbosity=2).run(test_suite)
    
    if test_result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")