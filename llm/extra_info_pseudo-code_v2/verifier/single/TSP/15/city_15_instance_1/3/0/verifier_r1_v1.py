import math
import unittest

# Given tour and cost solution
solution_tour = [0, 4, 10, 9, 3, 7, 1, 6, 14, 8, 12, 11, 2, 13, 5, 0]
solution_cost = 355.8278916013674

# Coordinates of cities
cities_coordinates = [
    (29, 51),  # Depot (city 0)
    (49, 20),  # City 1
    (79, 69),  # City 2
    (17, 20),  # City 3
    (18, 61),  # City 4
    (40, 57),  # City 5
    (57, 30),  # City 6
    (36, 12),  # City 7
    (93, 43),  # City 8
    (17, 36),  # City 9
    (4, 60),   # City 10
    (78, 82),  # City 11
    (83, 96),  # City 12
    (60, 50),  # City 13
    (98, 1),   # City 14
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
        self.assertEqual(len(solution_tour) - 2, len(set(solution_tour[1:-1])))
        self.assertCountEqual(set(solution_tour[1:-1]), set(range(1, 15)))
    
    def test_correct_travel_cost(self):
        "Check if the cost calculation is correct."
        calc_cost = sum(
            euclidean_distance(cities_coordinates[solution_tour[i]], cities_coordinates[solution_tour[i + 1]])
            for i in range(len(solution_tour) - 1)
        )
        self.assertAlmostEqual(calc_cost, solution_cost, places=5)
    
    def test_output_format(self):
        "Confirm that the output format of the tour is correct."
        self.assertTrue(isinstance(solution_tour, list))
        self.assertTrue(all(isinstance(x, int) for x in solution_tour))
        self.assertTrue(isinstance(solution_cost, float))

# Execute the test suite
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestTravelingSalesmanSolution))
runner = unittest.TextTestRunner()
result = runner.run(suite)

# Determine output message based on the test results
if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")