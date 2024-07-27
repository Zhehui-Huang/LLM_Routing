import unittest
import math

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 
            4: (54, 42), 5: (36, 30), 6: (52, 82), 7: (93, 44), 
            8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79), 
            12: (56, 58), 13: (72, 43), 14: (6, 99)
        }
        self.tour_solution = [0, 2, 13, 3, 4, 12, 11, 6, 0]
        self.total_cost_solution = 132.1185774560832

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour_solution[0], 0, "Tour should start at depot")
        self.assertEqual(self.tour_solution[-1], 0, "Tour should end at depot")

    def test_tour_visits_exactly_8_cities(self):
        # Plus one because the depot city is visited twice (start and end)
        self.assertEqual(len(set(self.tour_solution)), 8, "Tour should visit exactly 8 distinct cities, including the depot")

    def test_travel_costs(self):
        def euclidean_distance(p1, p2):
            return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

        calculated_cost = sum(euclidean_distance(self.cities[self.tour_solution[i]], self.cities[self.tour_solution[i+1]])
                               for i in range(len(self.tour_solution) - 1))
        
        self.assertAlmostEqual(calculated_cost, self.total_cost_solution, places=5, 
                               msg="Calculated tour cost should match the provided total cost")

    def test_output_format(self):
        # Requirement 5 implicitly checked by other tests: output format is a list of city indices and total cost

        # Check that the tour actually is a correct sequence of node visits
        for city_index in self.tour_solution[:-1]:
            self.assertIn(city_index, self.cities.keys(), "Each tour city must be a valid city index")
        
        self.assertIsInstance(self.tour_solution, list, "Tour should be a list of integers")
        self.assertIsInstance(self.total_cost_solution, float, "Total cost should be a float")

    def run_tests(self):
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(TestTourSolution))
        runner = unittest.TextTestRunner()
        result = runner.run(suite)
        if result.wasSuccessful():
            print("CORRECT")
        else:
            print("FAIL")

if __name__ == '__main__':
    test_solution = TestTourSolution()
    test_solution.run_tests()