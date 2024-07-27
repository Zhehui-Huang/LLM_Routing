import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.tour = [0, 3, 6, 2, 8, 9, 1, 5, 7, 4, 0]
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
        self.reported_total_distance = 320.8
        self.reported_max_distance = 61.7

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour should start at the depot city 0")
        self.assertEqual(self.tour[-1], 0, "Tour should end at the depot city 0")

    def test_visit_each_city_once(self):
        self.assertEqual(sorted(self.tour[1:-1]), sorted(list(self.cities.keys())[1:]), "Each city must be visited exactly once")

    def test_minimize_longest_distance_between_cities(self):
        max_distance = 0
        for i in range(len(self.tour)-1):
            x1, y1 = self.cities[self.tour[i]]
            x2, y2 = self.cities[self.tour[i+1]]
            distance = math.hypot(x2 - x1, y2 - y1)
            if distance > max_distance:
                max_distance = distance
        self.assertAlmostEqual(max_distance, self.reported_max_distance, places=1, msg="Reported max distance should match calculated max distance")

def run_tests():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestTSPSolution('test_tour_starts_and_ends_at_depot'))
    test_suite.addTest(TestTSPSolution('test_visit_each_city_once'))
    test_suite.addTest(TestTSPSolution('test_minimize_longest_distance_between_cities'))

    result = unittest.TextTestRunner().run(test_suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

if __name__ == "__main__":
    run_tests()