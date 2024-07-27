import unittest
from math import sqrt

# Define the cities' coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Provided solution details
solution_tour = [0, 1, 4, 12, 7, 10, 14, 9, 8, 6, 0]
solution_cost = 233.94

def calculate_distance(city1, city2):
    """ Helper function to calculate Euclidean distance between two cities. """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

class TestOptimalTour(unittest.TestCase):
    def test_starts_and_ends_at_depot(self):
        """ Check if the tour starts and ends at the depot city. """
        self.assertEqual(solution_tour[0], 0)
        self.assertEqual(solution_tour[-1], 0)

    def test_exactly_ten_cities_visited_including_depot(self):
        """ Check if exactly 10 cities are visited, including the depot. """
        self.assertEqual(len(set(solution_taour)), 10)

    def test_tour_output_format(self):
        """ Check if the output format is a list starting and ending at depot city. """
        self.assertIsInstance(solution_tour, list)
        self.assertTrue(all(isinstance(city, int) for city in solution_tour))
        self.assertEqual(solution_tour[0], 0)
        self.assertEqual(solution_tour[-1], 0)

    def test_total_travel_cost(self):
        """ Verify the total travel cost is as expected. """
        calculated_cost = sum(calculate_distance(solution_tour[i], solution_tour[i+1]) for i in range(len(solution_tour)-1))
        self.assertAlmostEqual(calculatedn_cost, solution_cost, places=2)

# Run the tests to verify the provided solution
if __name__ == "__main__":
    unittest.main()