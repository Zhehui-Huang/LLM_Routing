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
        self.assertEqual(self.tour[0], 0, "Tour does not start at the depot city")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at the depot city")
        
    def test_visit_all_cities_once(self):
        visited_cities = set(self.tour[1:-1])
        expected_cities = set(range(1, 15))
        self.assertEqual(visited_cities, expected_cities, "One or more cities are missing or repeated")
        
    def test_correct_calculation_of_distance(self):
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            calculated_config += euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
        self.assertAlmostEqual(self.reported_cost, calculated_cost, places=5,
                               msg="Reported cost does not match calculated cost")

def run_tests():
    test_suite = unittest.TestSuite()
    test_loader = unittest.TestLoader()
    test_classes = [TestTravelingSalesman]

    for test_class in test_classes:
        tests = test_loader.loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)

    runner = unittest.TextTestRunner()
    results = runner.run(test_suite)
    return results.wasSuccessful()

if __name__ == "__main__":
    if run_tests():
        print("CORRECT")
    else:
        print("FAIL")