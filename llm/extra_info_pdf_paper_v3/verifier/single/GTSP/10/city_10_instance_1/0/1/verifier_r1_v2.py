import unittest
from math import sqrt

def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class VerifyTourSolutions(unittest.TestCase):
    def setUp(self):
        self.depot = (53, 68)
        self.cities = {
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
        self.groups = [
            [5, 6, 7],
            [2, 3],
            [1, 9],
            [4, 8]
        ]
        self.solution_tour = [0, 9, 5, 3, 8, 0]
        self.actual_cost = 169.9409598467532
    
    def test_solution(self):
        # Start and end at the depot
        self.assertEqual(self.solution_tour[0], 0, "Tour does not start at depot")
        self.assertEqual(self.solution_tour[-1], 0, "Tour does not end at depot")
        
        # Visit exactly one city from each group
        visited_groups = {g: False for g in range(len(self.groups))}
        for city in self.solution_tour[1:-1]:
            for i, group in enumerate(self.groups):
                if city in group:
                    if visited_groups[i]:
                        self.fail(f"Group {i} is visited more than once")
                    visited_groups[i] = True
        self.assertTrue(all(visited_groups.values()), "Not all groups are visited exactly once")
        
        # Calculate travel cost
        calculated_cost = 0
        coordinates_list = [self.depot] + [self.cities[i] for i in self.solution_tour[1:-1]] + [self.depot]
        for i in range(len(coordinates_list) - 1):
            calculated_cost += euclidean_distance(coordinates_list[i], coordinates_list[i + 1])
        
        self.assertAlmostEqual(calculated_cost, self.actual_cost, places=5, msg="Travel cost does not match expected cost")

# Utility function to run all tests
def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(VerifyTourSolutions))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

# Perform test
if __name__ == "__main__":
    run_tests()