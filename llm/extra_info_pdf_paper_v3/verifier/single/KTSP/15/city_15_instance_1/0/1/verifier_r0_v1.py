import unittest
import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_travel_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        total_cost += calculate_euclidean_distance(*coordinates[city1], *coordinates[city2])
    return total_cost

class TestTspSolution(unittest.TestCase):
    def test_tsp_solution(self):
        coordinates = {
            0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 
            5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 
            10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
        }
        solution_tour = [0, 6, 1, 7, 3, 9, 0]
        expected_cost = 118.8954868377263

        # Check if the tour starts and ends at the depot city 0
        self.assertEqual(solution_tour[0], 0)
        self.assertEqual(solution_tour[-1], 0)

        # Check if the tour visits exactly 6 cities including the depot
        self.assertEqual(len(set(solution_tour)), 6)

        # Check the travel cost calculation
        calculated_cost = total_travel_cost(solution_tour, coordinates)
        self.assertAlmostEqual(expected_cost, calculated_cost, places=4)

# Run the tests
if __name__ == '__main__':
    unittest.main()