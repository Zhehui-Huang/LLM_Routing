import math
import unittest

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities_coordinates = [
            (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
            (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
            (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
            (64, 72), (14, 89)
        ]
        self.solution_tour = [0, 10, 15, 3, 6, 7, 16, 5, 9, 2, 14, 11, 1, 13, 18, 8, 0]
        self.total_cost = 317.2028678661435

    def test_starts_and_ends_at_depot(self):
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)

    def test_number_of_cities_visited(self):
        # Ensure exactly 16 different cities are visited, including depot
        unique_cities = set(self.solution_tour)
        self.assertEqual(len(unique_cities), 16)

    def test_total_distance_calculation(self):
        # Calculate the total computed travel cost
        computed_cost = 0
        for i in range(len(self.solution_tour)-1):
            city1 = self.cities_coordinates[self.solution_tour[i]]
            city2 = self.cities_coordinates[self.solution_tour[i + 1]]
            computed_cost += calculate_distance(city1, city2)

        self.assertAlmostEqual(self.total_cost, computed_cost, places=5)


# Running the tests
if __name__ == "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
    result = unittest.TextTestRunner(verbosity=2).run(test_suite)
    
    # Determine if the solution is correct based on test results
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")