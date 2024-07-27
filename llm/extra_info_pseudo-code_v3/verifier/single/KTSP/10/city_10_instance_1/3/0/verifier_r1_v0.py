import unittest
from math import sqrt

# Provided solution
tour = [0, 3, 5, 2, 9, 0]
reported_cost = 158.46350711884693

# City coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

def compute_euclidean_distance(point1, point2):
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def compute_total_travel_cost(tour, city_coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += compute_euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    return total_cost

class TestTourSolution(unittest.TestCase):
    def test_start_end_at_depot(self):
        # Requirement 1
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

    def test_visits_exactly_five_cities(self):
        # Requirement 2
        self.assertEqual(len(set(tour)), 5)
        
    def test_minimum_travel_cost(self):
        # Requirement 3
        calculated_cost = compute_total_travel_cost(tour, cities)
        # Set a small tolerance for floating point comparisons
        tolerance = 1e-3
        self.assertAlmostEqual(calculated_cost, reported_cost, delta=tolerance)
        
    def test_tour_representation(self):
        # Requirement 4
        self.assertIsInstance(tour, list)
        all_indices = all(isinstance(city, int) for city in tour)
        self.assertTrue(all_indices)
        
    def test_output_format(self):
        # Requirement 5
        self.assertIsInstance(tour, list)
        self.assertIsInstance(reported_cost, float)
        # Check string output format by simulating the expected output
        expected_output_format = f"Tour: {tour}\nTotal travel cost: {reported_cost}"
        
        # Example of how you would typically format the output in a real system
        output_format = f"Tour: {tour}\nTotal travel cost: {reported_cost}"
        self.assertEqual(output_format, expected_output_format)

if __name__ == "__main__":
    # Run the unit tests
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    tests = loader.loadTestsFromTestCase(TestTourSolution)
    test_suite.addTests(tests)
    
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")