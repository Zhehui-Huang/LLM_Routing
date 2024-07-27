import unittest
import math

# Fixed data provided
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Fixed solution tour as received
solution_tour = [0, 11, 9, 16, 17, 15, 5, 19, 3, 0, 18, 4, 1, 10]
solution_cost = 274.56551998731334  # Updated from your initial faulty solutions

def calculate_travel_cost(tour, city_locations):
    total_cost = 0
    for i in range(len(tour) - 1):
        start = city_locations[tour[i]]
        end = city_locations[tour[i + 1]]
        total_cost += math.sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)
    return total_cost

class TestTSPSolution(unittest.TestCase):
    def test_tour_starts_and_ends_at_depot(self):
        # Correcting checks to ensure depot city at tour start and end
        self.assertEqual(solution_tour[0], 0, "Tour should start at depot city.")
        self.assertEqual(solution_tour[-1], 0, "Tour should end at depot city.")

    def test_exact_number_of_cities_visited(self):
        # Checking for unique cities, excluding the repeated start/end depot
        self.assertEqual(len(set(solution_tour[:-1])), 13, "Should visit exactly 13 unique cities including the depot.")
        self.assertEqual(len(solution_tour), 14, "Tour should consist of 14 stops, 13 unique cities and one return.")

    def test_tour_path_cost(self):
        calculated_cost = calculate_travel_cost(solution_tour, cities)
        self.assertAlmostEqual(calculated_cost, solution_cost, delta=0.01,
                               msg="The calculated cost should closely match the provided expected cost.")

    def test_tour_output_format(self):
        self.assertIsInstance(solution_tour, list, "Tour output should be a list.")
        self.assertIsInstance(solution_cost, float, "Total travel cost should be a float.")

# Running the tests
if __name__ == "__main__":
    unittest.main()