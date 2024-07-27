import unittest
import math

class TestKTSPSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates of the cities
        self.cities = {
            0: (9, 93),
            1: (8, 51),
            10: (19, 65),
            8: (19, 76)
        }
        # Solution provided
        self.solution_tour = [0, 1, 10, 8, 0]
        self.solution_cost = 90.53947981328088

    def calculate_distance(self, city1, city2):
        return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
    
    def test_tour_start_end_at_depot(self):
        # Check if the tour starts and ends at the depot city
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)
    
    def test_exact_number_of_cities(self):
        # Check if exactly 4 cities are visited
        self.assertEqual(len(set(self.solution_tour)), 4)
    
    def test_correct_total_travel_cost(self):
        # Calculate the total travel cost for verification
        total_cost = 0
        for i in range(len(self.solution_tour) - 1):
            total_cost += self.calculate_distance(self.cities[self.solution_tour[i]], self.cities[self.solution_tour[i + 1]])
        self.assertAlmostEqual(total_cost, self.solution_cost, places=5)
    
    def test_output_format(self):
        # Check if the solution format is correct
        self.assertIsInstance(self.solution_tour, list)
        self.assertIsInstance(self.solution_cost, float)
        self.assertTrue(all(isinstance(city, int) for city in self.solution_tour))

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestKTSPSolution("test_tour_start_end_at_depot"))
    suite.addTest(TestKTSPSolution("test_exact_number_of_cities"))
    suite.addTest(TestKTSPSolution("test_correct_total_travel_cost"))
    suite.addTest(TestKTSPSolution("test_output_format"))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    if result.failures or result.errors:
        print("FAIL")
    else:
        print("CORRECT")

run_tests()