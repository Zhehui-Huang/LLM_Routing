import unittest
from math import sqrt

# Given cities coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Solution from user
solution_tour = [0, 6, 2, 13, 8, 9, 14, 0]
solution_cost = 130.6658168109853

def calculate_euclidean_distance(point1, point2):
    """ Calculate Euclidean distance between two points """
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def calculate_total_travel_cost(tour):
    """ Calculate the total travel distance of the tour """
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_distance

class TestVRPSolution(unittest.TestCase):
    def test_tour_start_end_city(self):
        """ Test if the tour starts and ends at the depot city (city 0) """
        self.assertEqual(solution_tour[0], 0, "Tour should start at city 0")
        self.assertEqual(solution_tour[-1], 0, "Tour should end at city 0")

    def test_tour_length(self):
        """ Test if exactly 7 cities are visited in the tour including the depot city """
        self.assertEqual(len(set(solution_tour)), 7, "Tour should visit exactly 7 cities including the depot")

    def test_tour_output_format(self):
        """ Test output format of the tour """
        self.assertIsInstance(solution_tour, list, "Tour should be a list of city indices")
        self.assertTrue(all(isinstance(city, int) for city in solution_tour), "Tour should contain only integer indices")

    def test_travel_cost_calculation(self):
        """ Test if the calculated travel cost matches the provided travel cost """
        calculated_cost = calculate_total_travel_cost(solution_tour)
        self.assertAlmostEqual(calculated_cost, solution_cost, places=5, msg="Calculated travel cost does not match the provided cost")

    def test_solution(self):
        """ Test all requirements to either pass or fail the solution """
        try:
            # Run all unittests except for the aborting ones
            test_suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestVRPSolution)
            test_result = unittest.TextTestRunner().run(test_suite)
            if test_result.wasSuccessful():
                print("CORRECT")
            else:
                print("FAIL")
        except Exception as e:
            print("FAIL")

# Execute all tests
if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)