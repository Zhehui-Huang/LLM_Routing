import unittest
import math

# Given coordinates of cities including depot locations
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Solution tours and other details
solution_tours = [0, 18, 13, 10, 17, 12, 14, 4, 16, 9, 7, 8, 3, 15, 2, 19, 0, 1, 6, 20, 5, 11, 1]
overall_total_cost = 348.2582480676432

class TestTSPSolution(unittest.TestCase):
    
    def test_city_count(self):
        # The environment should have 19 cities
        self.assertEqual(len(city_coordinates), 19)

    def test_all_cities_visited(self):
        # Extracting the unique cities visited from proposed solution except depots
        unique_cities_visited = set(abs(city) for city in solution_tours if city in city_coordinates)
        self.assertEqual(len(unique_cities_visited), len(city_coordinates))
    
    def test_correct_starting_positions(self):
        # Initial positions for both robots should be their respective depots
        self.assertEqual(solution_tours[0], 0)  # Robot 0 starting at depot 0
        self.assertEqual(solution_tours[len(solution_tours) - 1], 1)  # Robot 1 ending at depot 1

    def test_travel_cost(self):
        # Calculate the total distance for the given solution
        def calculate_distance(city1, city2):
            return math.sqrt((city_coordinates[city1][0] - city_coordinates[city2][0]) ** 2 + 
                             (city_coordinates[city1][1] - city_coordinates[city2][1]) ** 2)

        calculated_cost = 0
        for i in range(1, len(solution_tours)):
            calculated_cost += calculate_distance(abs(solution_tours[i-1]), abs(solution_tours[i]))
        
        # Check if the rounded calculated cost matches the given optimal cost (rounded to avoid floating-point issues)
        self.assertAlmostEqual(calculated_cost, overall_total_cost, places=5)

# Run the tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
test_result = unittest.TextTestRunner(verbosity=2).run(suite)

# Verify if all tests are passed
if test_result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")