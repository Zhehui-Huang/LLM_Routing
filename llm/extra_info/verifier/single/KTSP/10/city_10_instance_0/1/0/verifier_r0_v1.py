import unittest
import math

class TestRobotTour(unittest.TestCase):
    def test_robot_tour(self):
        def calculate_distance(city1, city2):
            return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)
        
        # Provided solution
        tour = [0, 9, 5, 6, 0]
        reported_travel_cost = 61.65991894151281
        
        # City coordinates
        cities = {
            0: (50, 42),
            1: (41, 1),
            2: (18, 46),
            3: (40, 98),
            4: (51, 69),
            5: (47, 39),
            6: (62, 26),
            7: (79, 31),
            8: (61, 90),
            9: (42, 49)
        }
        
        # [Requirement 1] Start and end at the depot city
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)
        
        # [Requirement 2] Tour must include exactly 4 distinct cities
        self.assertEqual(len(set(tour)) - 1, 3)  # Subtract 1 for the depot city count
        
        # [Requirement 3] Verify the reported travel cost
        calculated_cost = 0
        for i in range(len(tour)-1):
            calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
        
        # Using a tolerance in cost comparison because of potential floating-point arithmetic issues
        self.assertAlmostEqual(calculated_cost, reported_travel_cost, places=5)

# Execute the tests
if __name__ == '__main__':
    unittest.main()