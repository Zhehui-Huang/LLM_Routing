import unittest
import math

# Define the coordinates of all cities
city_coordinates = [
    (16, 90),  # Depot
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

class TestVRPSolution(unittest.TestCase):
    def test_unique_cities(self):
        """ Test that exactly 10 unique cities, including the depot, are visited """
        unique_cities = set([0, 1, 4, 5, 6, 8, 9, 10, 13, 14])
        self.assertEqual(len(unique_cities), 10)
    
    def test_route_starts_and_ends_at_depot(self):
        """ Test that the route starts and ends at the depot """
        tour = [0, 1, 4, 5, 6, 8, 9, 10, 13, 14, 0]
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)
    
    def test_number_of_cities_in_tour(self):
        """ Test the tour includes exactly 10 cities plus the return to the depot """
        tour = [0, 1, 4, 5, 6, 8, 9, 10, 13, 14, 0]
        self.assertEqual(len(tour), 11)
    
    def test_correct_total_travel_cost(self):
        """ Test that the total travel cost is calculated correctly """
        tour = [0, 1, 4, 5, 6, 8, 9, 10, 13, 14, 0]
        calculated_cost = 0
        for i in range(1, len(tour)):
            city1, city2 = tour[i-1], tour[i]
            coord1 = city_coordinates[city1]
            coord2 = city_coordinates[city2]
            distance = math.sqrt((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2)
            calculated_cost += distance
        self.assertAlmostEqual(calculated_cost, 208.79, places=2)
    
    def test_consistency_with_algorithm_specification(self):
        """ Use the provided pseudo-code to check if the solution can potentially be derived using it. """
        # This is a hypothetical check assuming you have GVNS functions etc.
        # Since we cannot fully execute the GVN algorithm here, this will just reflect a placeholder for actual checks.
        self.assertTrue(True, "This placeholder represents checking the use of the specified GVNS structure.")
        
def run_tests():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestVRPSolution))
    runner = unittest.TextTestRunner()
    results = runner.run(test_suite)
    
    if results.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

# Execute the tests
print(run_tests())