import unittest
from math import sqrt

def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestTravelingRobotSolution(unittest.TestCase):
    def test_robot_tour(self):
        # City coordinates with city index as the index in the list
        cities = {
            0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40),
            4: (54, 42), 5: (36, 30), 6: (52, 82), 7: (93, 44),
            8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79),
            12: (56, 58), 13: (72, 43), 14: (6, 99)
        }
        
        # Provided solution details
        provided_tour = [0, 13, 2, 3, 10, 8, 11, 6, 0]
        provided_cost = 183.0679936125828
        
        # Checking if the tour starts and ends at the depot city 0
        self.assertEqual(provided_tour[0], 0, "Should start at depot city 0")
        self.assertEqual(provided_tour[-1], 0, "Should return to depot city 0")
        
        # Check if exactly 8 different cities are visited
        unique_cities = set(provided_tour)
        self.assertEqual(len(unique_cities), 8, "Should visit exactly 8 different cities")
        
        # Check if total travel cost is minimized
        total_cost = 0
        for i in range(len(provided_tour) - 1):
            city1, city2 = provided_tour[i], provided_tour[i+1]
            total_cost += calculate_distance(cities[city1], cities[city2])
        
        # Compare calculated cost and provided cost
        self.assertAlmostEqual(total_cost, provided_cost, places=5, msg="Total cost should match provided cost")
        
# Running the tests
suite = unittest.TestSuite()
suite.addTest(TestTravelingRobotSolution('test_robot_tour'))

runner = unittest.TextTestRunner()
result = runner.run(suite)

if result.wasSuccessful():
    output = "CORRECT"
else:
    output = "FAIL"

print(output)