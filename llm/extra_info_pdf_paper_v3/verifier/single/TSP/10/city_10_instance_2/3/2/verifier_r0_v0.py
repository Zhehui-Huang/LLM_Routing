import unittest
from math import sqrt

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_tour_cost(tour, cities):
    """ Calculate the total travel distance of the tour """
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += calculate_distance(cities[tour[i-1]], cities[tour[i]])
    return total_cost

class TestTSPSolution(unittest.TestCase):
    def test_tsp_solution(self):
        cities = {
            0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54),
            5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)
        }
        solution_tour = [0, 3, 4, 6, 7, 5, 9, 1, 2, 8, 0]
        solution_cost = 374.95561767511776

        # [Requirement 2]
        self.assertEqual(solution_tour[0], 0, "Tour should start at the depot city.")
        self.assertEqual(solution_tour[-1], 0, "Tour should end at the depot city.")

        # [Requirement 1]
        self.assertEqual(len(solution_tour), len(set(solution_tour)), "Each city should be visited exactly once.")

        # [Requirement 3]
        calculated_cost = total_tour_cost(solution_tour, cities)
        self.assertAlmostEqual(calculated_cost, solution_cost, places=5, msg="Calculated travel cost does not match expected.")

        # [Requirement 4 & 5]
        self.assertIsInstance(solution_tour, list, "Output should be a list of city indices.")
        self.assertIsInstance(solution_cost, float, "Total travel cost should be a float.")
        
        print("CORRECT")

# Running the tests
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)