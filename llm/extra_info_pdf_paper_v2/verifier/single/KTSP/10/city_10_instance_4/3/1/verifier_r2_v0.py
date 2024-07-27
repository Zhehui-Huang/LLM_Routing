import unittest
import math

class TestKTSPSolution(unittest.TestCase):
    
    def setUp(self):
        # City coordinates as given in problem statement
        # Format: city_index: (x, y)
        self.cities = {
            0: (79, 15),
            1: (79, 55),
            2: (4, 80),
            3: (65, 26),
            4: (92, 9),
            5: (83, 61),
            6: (22, 21),
            7: (97, 70),
            8: (20, 99),
            9: (66, 62)
        }
        
        # Provided solution tour
        self.tour = [0, 1, 3, 4, 5, 7, 8, 9, 0]
        self.reported_cost = 363.6

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tur[0], 0, "Tour should start at depot city 0")
        self.assertEqual(self.tour[-1], 0, "Tour should end at depot city 0")
        
    def test_tour_visits_exactly_8_cities(self):
        unique_cities = set(self.tour)
        # Subtract one for the depot which is counted twice (start and end)
        self.assertEqual(len(unique_cities) - 1, 8, "Tour should visit exactly 8 unique cities excluding the double counted depot")
        
    def test_tour_length(self):
        self.assertEqual(len(self.tour), 9, "Tour length should be 9 including start/end at depot")
        
    def test_tour_cost(self):
        total_distance = 0
        for i in range(len(self.tour) - 1):
            city_a = self.cities[self.tour[i]]
            city_b = self.cities[self.tour[i+1]]
            distance = math.sqrt((city_b[0] - city_a[0]) ** 2 + (city_b[1] - city_a[1]) ** 2)
            total_distance += distance
        # Compare the calculated distance with reported cost within a small tolerance
        self.assertAlmostEqual(total_distance, self.reported_cost, places=1, msg="Calculated tour cost should be close to reported cost")

    def test_provided_solution(self):
        self.test_tour_starts_and_ends_at_depot()
        self.test_tour_visits_exactly_8_cities()
        self.test_tour_length()
        self.test_tour_cost()

# Execution of the tests
def run_tests():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestKTSPSolution('test_provided_solution'))
    
    runner = unittest.TextTestRunner()
    test_results = runner.run(test_suite)
    
    if test_results.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

# Call to execute the test suite
result = run_tests()
print(result)