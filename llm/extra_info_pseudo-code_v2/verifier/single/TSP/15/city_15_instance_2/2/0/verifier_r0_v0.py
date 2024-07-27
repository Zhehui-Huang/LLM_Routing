import unittest
import math

# Define the coordinates for each city where indices are city indices
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# Define the provided solution
tour_solution = [0, 6, 11, 8, 1, 14, 12, 4, 3, 10, 5, 9, 13, 7, 2, 0]
total_cost_solution = 322.5037276986899

# Function to calculate the total tour cost based on the `tour_solution`
def calculate_tour_cost(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Create a test class
class TestTourSolution(unittest.TestCase):
    
    def test_tour_start_end_at_depot(self):
        """ Requirement 1 & 6: The tour should start and end at the depot city 0. """
        self.assertEqual(tour_solution[0], 0)
        self.assertEqual(tour_solution[-1], 0)
    
    def test_tour_visits_all_cities_once(self):
        """ Requirement 2: Tour must visit all 14 other cities exactly once. """
        expected_cities = set(range(15))  # Set of all cities from 0 to 14
        tour_cities_set = set(tour_solution)
        self.assertEqual(tour_cities_set, expected_cities)
        self.assertTrue(all(tour_solution.count(city) == 1 for city in tour_cities_set))

    def test_travel_cost_calculation(self):
        """ Requirement 4: Travel cost must be calculated as the Euclidean distance. """
        calculated_cost = calculate_tour_cost(tour_solution)
        self.assertAlmostEqual(calculated_cost, total_cost_solution, places=5)
    
    def test_output_format(self):
        """ Requirement 6: Check format and tour structure """
        self.assertIsInstance(tour_solution, list)
        self.assertIsInstance(total_cost_solution, float)

# Run the tests
if __name__ == '__main__':
    unittest.main()