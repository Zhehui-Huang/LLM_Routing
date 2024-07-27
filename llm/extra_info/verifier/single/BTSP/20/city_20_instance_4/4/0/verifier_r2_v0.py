import unittest
import math

def compute_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestSolutionVerification(unittest.TestCase):
    def setUp(self):
        self.coordinates = [
            (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), 
            (69, 22), (28, 11), (70, 2), (47, 50), (60, 29), 
            (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), 
            (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
        ]
        self.tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 15, 4, 3, 19, 0]
        self.total_cost = 410.03585920085146
        self.max_distance = 89.00561780022652

    def test_start_and_end_at_depot(self):
        # Requirement 1
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_each_city_once(self):
        # Requirement 2
        visited = set(self.tour)
        self.assertEqual(len(visited), len(self.coordinates))
        self.assertEqual(visited, set(range(len(self.coordinates))))

    def test_correctly_computed_total_travel_cost(self):
        # Requirement 6
        computed_cost = sum(compute_distance(self.coordinates[self.tour[i]], self.coordinates[self.tour[i + 1]]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(computed_cost, self.total_cost, places=5)

    def test_correctly_computed_max_distance(self):
        # Requirement 7
        computed_max_distance = max(compute_distance(self.coordinates[self.tour[i]], self.coordinates[self.tour[i + 1]]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(computed_max_distance, self.max_distance, places=5)

    def test_output_tour_as_list_of_city_indices(self):
        # Requirement 5
        self.assertIsInstance(self.tour, list)
        all_indices = all(isinstance(city, int) for city in self.tour)
        self.assertTrue(all_indices)

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    test_suite.addTests(loader.loadTestsFromTestCase(TestSolutionVerification))

    # Run the tests
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)

    # Check if all tests passed
    if result.wasSuccessful():
        print("CORRECT")
    else:
/status/buff:        print("FAIL")