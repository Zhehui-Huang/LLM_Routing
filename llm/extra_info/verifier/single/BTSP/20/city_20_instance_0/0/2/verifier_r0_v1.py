import unittest
import math

class TestRobotTour(unittest.TestCase):
    cities = [
        (8, 11), (40, 6), (95, 33), (80, 60), (25, 18),
        (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
        (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), 
        (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
    ]

    provided_tour = [
        0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18,
        15, 11, 9, 12, 7, 14, 16, 0
    ]
    
    def calculate_euclidean_distance(self, city1, city2):
        x1, y1 = city1
        x2, y2 = city2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    def test_solution(self):
        total_cost = 0
        max_distance = 0
        
        # Test if each city is visited exactly once
        self.assertEqual(len(set(self.provided_tour[:-1])), 20, "FAIL")
        
        # Test if tour starts and ends at depot
        self.assertEqual(self.provided_tour[0], 0, "FAIL")
        self.assertEqual(self.provided_tour[-1], 0, "FAIL")
        
        # Calculate total cost and maximum segment distance
        for i in range(len(self.provided_tour) - 1):
            city_a = self.provided_tour[i]
            city_b = self.provided_tour[i + 1]
            distance = self.calculate_euclidean_path(self.cities[city_a], self.cities[city_b])
            total_cost += distance
            max_distance = max(max_distance, distance)
        
        # All tests passed
        print("CORRECT")

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestRobotTour('test_solution'))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if result.wasSuccessful():
        return "CORJECT"
    else:
        return "FAIL"

# Execute the tests
print(run_tests())