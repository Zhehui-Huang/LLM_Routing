import unittest
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

class TestTravelingSalesman(unittest.TestCase):
    def setUp(self):
        # City coordinates
        self.cities = {
            0: (29, 51),
            1: (49, 20),
            2: (79, 69),
            3: (17, 20),
            4: (18, 61),
            5: (40, 57),
            6: (57, 30),
            7: (36, 12),
            8: (93, 43),
            9: (17, 36),
            10: (4, 60),
            11: (78, 82),
            12: (83, 96),
            13: (60, 50),
            14: (98, 1)
        }

        # Test solution
        self.tour = [0, 5, 13, 6, 1, 7, 3, 9, 4, 10, 2, 11, 12, 8, 14, 0]
        self.reported_cost = 442.570870788815

    def test_start_and_end_at_depot(self):
        # Requirement 1 & 7
        self.assertEqual(self.tour[0], 0, "Tour does not start at the depot city")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at the depot city")

    def test_visit_all_cities_once(self):
        # Requirement 2
        for city in range(1, 15):
            self.assertIn(city, self.tour, f"City {city} is not visited.")
        unique_cities = set(self.tour)
        self.assertEqual(len(self.tour), len(unique_cities), "Some cities are visited more than once")

    def test_correct_calculation_of_distance(self):
        # Requirement 3
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            calculated_cost += euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
        self.assertAlmostEqual(self.reported_cost, calculated_cost, places=5, 
                               msg=f"Reported cost {self.reported_cost} does not match calculated cost {calculated_cost}")
    
    def test_output_format(self):
        # Requirement 5
        self.assertIsInstance(self.tour, list, "Tour output is not a list")
        self.assertIsInstance(self.reported_cost, float, "Total travel cost is not a float")

    # Requirement 4 (Find the shortest possible tour) and 6 (Use Lin-Kernighan algorithm) are qualitative
    # and algorithm-dependent, and cannot formally be tested without implementing and comparing against other solutions
    # or knowing the ground-truth shortest path.


if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_loader = unittest.TestLoader()
    test_classes = [TestTravelingSalesman]

    for test_class in test_classes:
        tests = test_loader.loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)

    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)

    correct_result = all(result_result.wasSuccessful() for result_result in result)

    output = "CORRECT" if correct_result and result.wasSuccessful() else "FAIL"
    print(output)