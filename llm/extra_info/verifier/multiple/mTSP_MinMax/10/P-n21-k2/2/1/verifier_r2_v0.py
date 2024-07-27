import unittest
from math import sqrt

# Constants
COORDINATES = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

def calculate_distance(city1, city2):
    x1, y1 = COORDINATES[city1]
    x2, y2 = COORDINATES[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

class TestTSPValidation(unittest.TestCase):
    
    def test_unique_cities_visit(self):
        robot_0_tour = [0, 20, 5, 15, 4, 18, 6, 3, 17, 13, 7, 0]
        robot_1_tour = [0, 16, 19, 10, 2, 11, 12, 14, 1, 8, 9, 0]

        total_cities_visited = set(robot_0_tour[1:-1] + robot_1_tour[1:-1])
        
        self.assertEqual(len(total_cities_visited), 20, "Not all cities are visited exactly once.")
    
    def test_tour_validity(self):
        robot_0_tour = [0, 20, 5, 15, 4, 18, 6, 3, 17, 13, 7, 0]
        robot_1_tour = [0, 16, 19, 10, 2, 11, 12, 14, 1, 8, 9, 0]

        # Check start and end at the depot
        self.assertTrue(robot_0_tour[0] == robot_0_tour[-1] == 0, "Robot 0 tour does not start and end at the depot.")
        self.assertTrue(robot_1_tour[0] == robot_1_tour[-1] == 0, "Robot 1 tour does not start and end at the depot.")
        
        # Check for repeating visits within a tour
        self.assertEqual(len(robot_0_tour), len(set(robot_0_tour)), "Robot 0 revisits cities.")
        self.assertEqual(len(robot_1_tour), len(set(robot_1_tour)), "Robot 1 revisits cities.")

    def test_travel_cost_accuracy(self):
        robot_0_tour = [0, 20, 5, 15, 4, 18, 6, 3, 17, 13, 7, 0]
        robot_1_tour = [0, 16, 19, 10, 2, 11, 12, 14, 1, 8, 9, 0]

        # Calculating total cost
        def total_cost(tour):
            return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        
        calculated_cost_0 = total_cost(robot_0_tour)
        calculated_cost_1 = total_cost(robot_1_tour)
        
        # Given costs
        given_cost_0 = 235.95852071531732
        given_cost_1 = 268.96337868697583

        self.assertAlmostEqual(calculated_cost_0, given_cost_0, places=5, msg="Cost calculation error for Robot 0.")
        self.assertAlmostEqual(calculated_cost_1, given_cost_1, places=5, msg="Cost calculation error for Robot 1.")

# Running the tests
if __name__ == '__main__':
    result = unittest.main(argv=[''], exit=False)
    if result.result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")