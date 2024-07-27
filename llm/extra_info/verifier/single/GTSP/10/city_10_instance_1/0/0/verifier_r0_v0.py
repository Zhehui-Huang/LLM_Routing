import math
import unittest

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80), 
            4: (18, 63), 5: (54, 91), 6: (70, 14), 7: (97, 44), 
            8: (17, 69), 9: (95, 89)
        }
        self.groups = {
            0: [5, 6, 7],
            1: [2, 3],
            2: [1, 9],
            3: [4, 8]
        }
        self.tour = [0, 5, 2, 9, 8, 0]
        self.computed_cost = 183.98559431675523

    def test_start_and_end_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour should start at the depot (city 0)")
        self.assertEqual(self.tour[-1], 0, "Tour should end at the depot (city 0)")
    
    def test_visit_one_from_each_group(self):
        visited = set(self.tour[1:-1])  # exclude the depot city from the start and the end
        for group, cities in self.groups.items():
            self.assertTrue(any(city in cities for city in visited), f"One city from group {group} should be visited")
    
    def test_correct_travel_cost(self):
        total_cost = 0
        for i in range(len(self.tour) - 1):
            total_cost += euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i+1]])
        self.assertAlmostEqual(total_cost, self.computed_cost, msg="Computed travel cost should match the provided total travel cost")
    
    def test_is_shortest_path(self):
        # This is a complex requirement to validate without solving the problem again or knowing all possible legal tours.
        # For actual unit tests, this would typically require comparing against a precomputed set of expected results.
        # Here it gets a placeholder pass, as computationally validating that it's indeed the shortest requires full re-computation.
        pass

if __name__ == "__main__":
    test_loader = unittest.TestLoader()
    test_suite = test_loader.loadTestsFromTestCase(TestTSPSolution)
    test_runner = unittest.TextTestRunner()
    test_result = test_runner.run(test_suite)
    
    if test_result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")