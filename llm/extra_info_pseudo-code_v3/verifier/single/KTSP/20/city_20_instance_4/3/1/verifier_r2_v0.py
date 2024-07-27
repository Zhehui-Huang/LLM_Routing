import unittest
from math import sqrt

# City coordinates are given in the problem statement
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Proposed solution tour and cost
solution_tour = [0, 2, 14, 1, 8, 17, 11, 13, 5, 7, 12, 15, 10, 6, 4, 3, 0]
solution_cost = 460.95668696003327

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        start_city = cities[tour[i]]
        end_city = cities[tour[i + 1]]
        distance = sqrt((end_city[0] - start_city[0]) ** 2 + (end_city[1] - start_city[1]) ** 2)
        total_cost += distance
    return total_cost

class TestTSPSolution(unittest.TestCase):
    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(solution_tour[0], 0, "Tour does not start at the depot city")
        self.assertEqual(solution_tour[-1], 0, "Tour does not end at the depot city")

    def test_tour_visits_exactly_16_cities(self):
        self.assertEqual(len(set(solution_tour)), 16, "Tour does not visit exactly 16 cities")

    def test_travel_cost_calculation(self):
        # Compute the travel cost from the provided tour
        computed_cost = calculate_tour_cost(solution_tour)
        self.assertAlmostEqual(computed_cost, solution_cost, places=5, msg="Computed tour cost is incorrect")

    def test_complete_tour_return_to_depot(self):
        self.assertEqual(solution_tour[-1], solution_tour[0], "Tour does not return to the depot")

    def test_output_format(self):
        self.assertIsInstance(solution_tour, list, "Output format for tour is incorrect")
        self.assertIsInstance(solution_cost, float, "Output format for travel cost is incorrect")

    def test_algorithm_implementation_correctness(self):
        # Difficult to test fully without an actual implementation function provided.
        # Here we could normally test if the actual implementation was used.
        # This is a placeholder to remind to test the actual GVNS algorithm functions.
        pass

unittest.main(argv=[''], verbosity=2, exit=False)