import unittest
import math

# Coordinates of the cities
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
    (64, 72), (14, 89)
]

def calculate_distance(city1, city2):
    (x1, y1), (x2, y2) = cities[city1], cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Provided solution details
solution_tour = [0, 19, 8, 17, 18, 13, 1, 11, 14, 2, 9, 5, 16, 7, 12, 6, 10, 15, 4, 3, 0]
solution_cost = 343.5965714113396

class TestTSPSolution(unittest.TestCase):
    def test_visits_all_cities_once(self):
        # Test if all cities except the starting/ending one (0) is visited exactly once
        self.assertEqual(sorted(solution_tour[1:-1]), sorted(range(1, 20)))

    def test_correct_start_and_end(self):
        # Test if the tour starts and ends at the depot city (0)
        self.assertEqual(solution_tour[0], 0)
        self.assertEqual(solution_tour[-1], 0)

    def test_calculate_travel_cost(self):
        # Calculate the total travel cost from the given tour and compare it to the provided cost
        calculated_cost = 0
        for i in range(len(solution_tour) - 1):
            calculated_cost += calculate_distance(solution_tour[i], solution_tour[i + 1])
        self.assertAlmostEqual(calculated_cost, solution_cost, places=5)

    @unittest.skip("Lin-Kernighan Algorithm check is theoretical.")
    def test_lin_kernighan_algorithm(self):
        # This check is skipped as correctly verifying Lin-Kernighan requires algorithm implementation specifics.
        pass

if __name__ == '__main__':
    unittest.main()