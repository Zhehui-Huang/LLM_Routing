import unittest
from math import sqrt

# Provided cities data redefined for testing purpose
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

def calculate_distance(city1, city2):
    """Helper function to calculate Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

class TestRobotTours(unittest.TestCase):
    def test_solution(self):
        tours = [
            [0, 1, 4, 10, 2, 3, 8, 9, 7, 5, 6, 0],
            [0, 16, 11, 15, 12, 19, 18, 13, 17, 14, 20, 0]
        ]
        # Calculating total distances
        robot_costs = []
        for tour in tours:
            cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
            robot_costs.append(cost)
            
        total_cost = sum(robot_costs)
        
        # Actual reported costs
        reported_robot_costs = [131.03562107117372, 145.75885545934872]
        reported_total_cost = 276.79447653052245
        
        # Verify each robot's total travel cost
        for calculated_cost, reported_cost in zip(robot_costs, reportedrobe_costs):
            self.assertAlmostEqual(calculated_cost, reported_cost, places=5)
        
        # Verify total overall cost
        self.assertAlmostEqual(total_cost, reported_total_cost, places=5)
        
        # Verify unique city visitation and return to depot
        all_cities_visited = set()
        for tour in tours:
            self.assertEqual(tour[0], 0)  # start at depot
            self.assertEqual(tour[-1], 0)  # end at depot
            all_cities_visited.update(tour[1:-1])
            
        # Check all cities are visited exactly once
        self.assertEqual(all_cities_visited, set(range(1, 21)))

# Running the tests
if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestRobotTours))
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
    
    # Output the result based on tests
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")