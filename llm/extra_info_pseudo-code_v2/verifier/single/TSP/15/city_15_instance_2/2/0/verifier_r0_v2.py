import unittest
import math

# Define the coordinates for each city where indices are city indices
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Provided solution
tour_solution = [0, 6, 11, 8, 1, 14, 12, 4, 3, 10, 5, 9, 13, 7, 2, 0]
total_cost_solution = 322.5037276986899

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Calculate tour cost from the provided solution
def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Assertion class for testing
class TestTourSolution(unittest.TestCase):
    
    def test_tour_start_end_at_depot(self):
        # Requirement 1 & 6: Check start and end at depot
        self.assertEqual(tour_solution[0], 0)
        self.assertEqual(tour_solution[-1], 0)

    def test_tour_visits_all_cities_once(self):
        # Requirement 2: All cities except the depot should be visited exactly once
        self.assertEqual(len(set(tour_solution[1:-1])), 14)

    def test_proper_tour_calculation(self):
        # Requirement 4: Travel cost must be calculated correctly.
        calculated_cost = calculate_tour_cost(tour_solution)
        self.assertAlmostEqual(calculated_cost, total_cost_solution, places=5)

    def test_output_format(self):
        # Requirement 6: Output verification
        self.assertIsInstance(tour_solution, list)
        self.assertIsInstance(total_cost_solution, float)

# Running the tests
if __name__ == '__main__':
    unittest.main()