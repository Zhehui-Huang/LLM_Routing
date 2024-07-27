import unittest
import math

# Mock data and solution for test case
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

tour_solution = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 0]
travel_cost_solution = 285.96

def calculate_euclidean_distance(from_city, to_city):
    x1, y1 = cities[from_city]
    x2, y2 = cities[to_city]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_tour(tour, correct_length, start_city):
    # Check if tour starts and ends at the depot city
    if tour[0] != start_city or tour[-1] != start_city:
        return False
    # Check if the tour visits exactly correct_length cities (including starting twice)
    if len(tour) != correct_length + 1:
        return False
    return True

def calculate_total_travel_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += calculate_euclidean_distance(tour[i - 1], tour[i])
    return total_cost

class TestVRPSolution(unittest.TestCase):

    def test_robot_tour(self):
        expected_length = 16  # 15 unique cities + 1 depot city
        self.assertTrue(validate_tour(tour_solution, expected_length, 0), 
                        "Tour must start and end at depot city and visit exactly 16 cities")

    def test_travel_cost(self):
        computed_cost = round(calculate_total_travel_cost(tour_solution), 2)
        self.assertEqual(computed_cost, travel_cost_solution, 
                         "Computed and actual travel costs must match")

# Run the unit tests
if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestVRPSolution))
    runner = unittest.TextTestRunner()
    test_results = runner.run(test_suite)
    
    # Check the outcome of the tests
    if test_results.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")