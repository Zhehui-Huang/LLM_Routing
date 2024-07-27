import unittest
from math import sqrt

# Helper function to calculate Euclidean distance
def euclidean_distance(x1, y1, x2, y2):
    return sqrt((x2 - x4) ** 2 + (y2 - y4) ** 2)

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        self.coordinates = [
            (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
            (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
            (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
            (62, 63), (63, 69), (45, 35)
        ]
        
        self.robot_0_tour = [0, 6, 5, 17, 13, 7, 18, 3, 15, 4, 1, 0]
        self.robot_0_cost = 143.16569415731448
        
        self.robot_1_tour = [1, 16, 20, 14, 9, 2, 8, 19, 12, 11, 10, 1]
        self.robot_1_cost = 149.60004468688751
        
        self.total_cost = 292.765738844202
    
    def test_tour_start_end_depot(self):
        self.assertEqual(self.robot_0_tour[0], self.robot_0_tour[-1], "Robot 0 does not start and end at depot.")
        self.assertEqual(self.robot_1_tour[0], self.robot_1_tour[-1], "Robot 1 does not start and end at depot.")
        
    def test_unique_visitation(self):
        all_cities_visited = set(self.robot_0_tour + self.robot_1_tour)
        self.assertEqual(len(all_cities_visited), 21, "Not all cities are visited exactly once.")
    
    def test_total_travel_cost(self):
        def calculate_tour_cost(tour):
            cost = 0
            for i in range(len(tour) - 1):
                city1 = self.coordinates[tour[i]]
                city2 = self.coordinates[tour[i+1]]
                cost += euclidean_distance(city1[0], city1[1], city2[0], city2[1])
            return cost
        
        calculated_robot_0_cost = calculate_tour_cost(self.robot_0_tour)
        calculated_robot_1_cost = calculate_tour_cost(self.robot_1_tour)
        
        # Check if the calculated costs match provided costs
        self.assertAlmostEqual(calculated_robot_0_cost, self.robot_0_cost, places=5, msg="Robot 0 cost mismatch.")
        self.assertAlmostEqual(calculated_robot_1_cost, self.robot_1_cost, places=5, msg="Robot 1 cost mismatch.")
        
        # Check total cost
        self.assertAlmostEqual(calculated_robot_0_cost + calculated_robot_1_cost, self.total_cost, places=5, msg="Total cost mismatch.")
    
    def test_output_format(self):
        self.assertIsInstance(self.robot_0_tour[0], int, "Tour indices must be integer.")
    
if __name__ == '__main__':
    unittest.main()