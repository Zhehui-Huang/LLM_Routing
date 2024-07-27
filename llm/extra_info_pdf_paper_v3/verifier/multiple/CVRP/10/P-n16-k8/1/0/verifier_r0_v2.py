import unittest
import math

# City coordinates and demands
city_coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}
city_demand = {
    0: 0, 1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15, 8: 28,
    9: 8, 10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11
}
robots_tours = [
    [0, 6, 0], [0, 2, 0], [0, 1, 0], [0, 4, 15, 0], [0, 8, 0],
    [0, 7, 5, 0], [0, 14, 9, 13, 0], [0, 3, 12, 0], [0, 10, 11, 0]
]

def calculate_distance(city1, city2):
    coord1, coord2 = city_coords[city1], city_coords[city2]
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

class TestRobotRoutes(unittest.TestCase):
    def test_correct_solution(self):
        total_cost = 0
        total_calculated_cost = 495.31
        demands_covered = {i: 0 for i in range(1, 16)}
        
        for tour in robots_tours:
            prev_city = tour[0]
            trip_cost = 0
            
            for city in tour[1:]:
                demands_covered[city] += city_demand[city]
                trip_cost += calculate_distance(prev_city, city)
                prev_city = city
                
            trip_cost += calculate_distance(prev_city, tour[0])  # Return to depot cost
            total_cost += trip_cost
        
        self.assertAlmostEqual(total_cost, total_calculated_cost, "Total cost mismatch.")
        
        for city, demand in city_demand.items():
            if city != 0:  # Exclude depot
                self.assertEqual(demands_covered[city], demand, f"Demand for city {city} not met correctly.")

def run_tests():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestRobotRoutes('test_correct_solution'))
    
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
    
    # Output based on the test results
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

run_tests()