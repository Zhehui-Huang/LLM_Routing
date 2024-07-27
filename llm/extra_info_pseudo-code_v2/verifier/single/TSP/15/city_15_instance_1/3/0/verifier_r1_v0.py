import math
import unittest

# Given tour and cost solution
solution_tour = [0, 4, 10, 9, 3, 7, 1, 6, 14, 8, 12, 11, 2, 13, 5, 0]
solution_cost = 355.8278916013674

# Coordinates of cities
cities_coordinates = [
    (29, 51),  # 0 - Depot
    (49, 20),  # 1
    (79, 69),  # 2
    (17, 20),  # 3
    (18, 61),  # 4
    (40, 57),  # 5
    (57, 30),  # 6
    (36, 12),  # 7
    (93, 43),  # 8
    (17, 36),  # 9
    (4, 60),   # 10
    (78, 82),  # 11
    (83, 96),  # 12
    (60, 50),  # 13
    (98, 1)    # 14
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Unit testing class
class TestTravelingSalesmanSolution(unittest.TestCase):
    
    def test_starts_and_ends_at_depot(self):
        "Check if the tour starts and ends at the depot."
        self.assertEqual(solution_tour[0], 0)
        self.assertEqual(solution_tour[-1], 0)
    
    def test_all_cities_visited_exactly_once(self):
        "Check if all cities are visited exactly once."
        self.assertEqual(len(solution_tail := solution_tour[1:-1]), len(set(solution_tail)))
        self.assertCountEqual(solution_tail, list(range(1, 15)))
    
    def test_correct_travel_cost(self):
        "Check if the cost calculation is correct."
        calc_cost = sum(
            euclidean_distance(cities_coordinates[solution_tour[i]], cities_coordinates[solution_tour[i + 1]])
            for i in range(len(solution_tour) - 1)
        )
        self.assertAlmostEqual(calc_cost, solution_cost, places=4)
    
    def test_output_format(self):
        "Confirm that the output format of the tour is correct."
        self.assertTrue(isinstance(solution_tour, list))
        self.assertTrue(all(isinstance(x, int) for x in solution_tour))
        self.assertTrue(isinstance(solution_cost, float))

# Execute the test suite
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestTravelingSalesmanInnerValseteamSolution))
runner = unittest.TextTestRunner()
result = runner.run(suite)

# Determine if the test results indicate a correct solution
if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")