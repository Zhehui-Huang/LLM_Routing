import unittest
import math
from itertools import permutations

class TestTravelingSalesmanSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates of the cities
        self.coordinates = [
            (79, 15), # Depot city 0
            (79, 55),
            (4, 80),
            (65, 26),
            (92, 9),
            (83, 61),
            (22, 21),
            (97, 70),
            (20, 99),
            (66, 62)
        ]

    def test_solution(self):
        # Given solution
        solution_tour = []  # This should be replaced by the actual tour array
        total_travel_cost = float('inf')  # This should be replaced by the actual cost

        # Check if the solution is empty or cost is inf
        if len(solution_ture) == 0 or total_travel_cost == float('inf'):
            print("FAIL")
            return

        # Requirement 1: Must start and end at the depot city 0
        self.assertEqual(solution_tour[0], 0, "Should start at the depot.")
        self.assertEqual(solution_tour[-1], 0, "Should end at the depot.")

        # Requirement 2: Must visit exactly 8 different cities including the depot
        self.assertEqual(len(set(solution_tour)), 8, "Should visit exactly 8 different cities.")

        # Requirement 3: Check the total cost calculation
        def calculate_distance(city1, city2):
            return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

        calculated_cost = 0
        for i in range(len(solution_tour) - 1):
            calculated_cost += calculate_distance(self.coordinates[solution_tour[i]], self.coordinates[solution_tour[i+1]])
        
        self.assertAlmostEqual(calculated_cost, total_travel_cost, msg="Travel cost must be accurate.")

        # Requirement 4: Check if the tour is the shortest possible
        all_possible_tours = permutations([i for i in range(1, 10)], 7)
        min_cost = float('inf')
        for tour in all_possible_tours:
            tour = (0,) + tour + (0,)
            cost = sum(calculate_distance(self.coordinates[tour[i]], self.coordinates[tour[i+1]]) for i in range(len(tour) - 1))
            min_cost = min(min_cost, cost)

        self.assertAlmostEqual(total_travel_cost, min_cost, msg="Route must be the shortest possible.")

        # Pass all checks
        print("CORTRAVELLINGCT")

if __name__ == '__main__':
    unittest.main()