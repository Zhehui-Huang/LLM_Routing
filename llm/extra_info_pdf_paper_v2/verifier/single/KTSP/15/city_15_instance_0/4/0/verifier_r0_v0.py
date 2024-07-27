import unittest
from math import sqrt

# Solution provided
solution_tour = [0, 8, 10, 11, 0]
solution_cost = 110.00961484483386

# City coordinates
cities = [
    (9, 93),   # Depot city 0
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

def calculate_euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_total_travel_cost(tour):
    return sum(calculate_euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

class TestTSPSolution(unittest.TestCase):
    def test_solution(self):
        # Requirement 1: Check if the robot starts and ends at depot city 0
        self.assertEqual(solution_tour[0], 0, "The tour does not start at city 0")
        self.assertEqual(solution_tour[-1], 0, "The tour does not end at city 0")
        
        # Requirement 2: Check if exactly 4 cities are visited including depot
        self.assertEqual(len(set(solution_tour)), 4, "The tour does not visit exactly 4 cities including the depot")

        # Requirement 5: Check the output format of the tour
        self.assertIsInstance(solution_tour, list, "Tour output is not a list")
        self.assertTrue(all(isinstance(city, int) for city in solution_tour), "Tour contains non-integer indices")

        # Requirement 6: Check the output format of the travel cost
        calculated_cost = calculate_total_travel_cost(solution_tour)
        self.assertAlmostEqual(calculated_cost, solution_cost, places=5, msg="Calculated travel cost does not match the provided cost")
    
    # Requirement 7: This requirement focuses on the input configuration which is assumed to be correctly provided and does not need testing in this scenario.

# Run the test case
suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
result = unittest.TextTestRunner(verbosity=0).run(suite)

if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")