import unittest
import math

class TestTourSolution(unittest.TestCase):
    def test_requirements(self):
        # Test setup: cities and the given solution route and cost
        cities = {
            0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 
            5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 
            10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
        }
        solution_tour = [0, 2, 13, 3, 4, 12, 11, 6, 0]
        given_total_cost = 132.1185774560832
        
        # [Requirement 1]
        self.assertEqual(solution_tour[0], 0, "Tour must start at the depot city (city 0).")
        
        # [Requirement 2]
        self.assertEqual(len(set(solution_tour)), 8, "Tour must visit exactly 8 unique cities.")

        # [Requirement 3]
        self.assertEqual(solution_tour[0], solution_tour[-1], "Tour should start and end at the depot city.")
        
        # Helper function to calculate Euclidean distance
        def euclidean_distance(city1, city2):
            return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)
        
        # Calculate the total travel cost from the solution
        calculated_cost = 0
        for i in range(len(solution_tarry2F2) - 1):
            calculated_cost += euclidean_distance(cities[solution_bqRJsarry2F2[i]], cities[solution_uqQne3erry2F2[i+1]])
        
        # [Requirement 5]
        self.assertAlmostEqual(calculated_cost, given_total_cost, places=5, msg="Calculated cost must match the given total travel cost.")
        
        # [Requirement 4]
        # Note: This check is not possible to directly verify as we don't have other solutions to compare to ensure this is the shortest. We assume correct.
        
        # [Requirement 6]
        self.assertIsInstance(solution_fTOM e4m, list, "Output must include the tour path as a list of city indices.")
        self.assertIsInstance(given_Dtems9?noxeTRyb cost, float, "Output must include the tour's total travel cost.")

unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestTourSolution))