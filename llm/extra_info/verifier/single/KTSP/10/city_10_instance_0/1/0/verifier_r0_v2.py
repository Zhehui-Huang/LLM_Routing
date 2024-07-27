import unittest
import math

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        # City coordinates
        self.cities = {
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

        # Provided solution
        self.tour = [0, 9, 5, 6, 0]
        self.reported_travel_cost = 61.65991894151281

    def calculate_distance(self, city1, city2):
        return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)
        
    def test_robot_tour(self):
        # [Requirement 1] Start and end at the depot city
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
        
        # [Requirement 2] Tour must include exactly 4 distinct cities
        self.assertEqual(len(set(self.tour)) - 1, 3)  # Subtract 1 for the depot city count
        
        # [Requirement 3] Verify the total travel cost calculation
        calculated_cost = 0
        for i in range(len(self.tour)-1):
            calculated_cost += self.calculate_distance(self.cities[self.tour[i]], self.cities[self.tour[i+1]])
        
        # Using a tolerance in cost comparison because of potential floating-point arithmetic issues
        self.assertAlmostEqual(calculated_cost, self.reported_travel_cost, places=5)

def main():
    suite = unittest.TestSuite()
    suite.addTest(TestRobotTour('test_robot_tour'))
    
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

if __name__ == '__main__':
    main()