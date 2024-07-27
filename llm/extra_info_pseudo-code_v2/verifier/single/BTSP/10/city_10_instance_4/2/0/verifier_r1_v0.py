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
        self.assertEqual(self.tour[0], 0, "Tour should start at the depot 0")
        self.assertEqual(self.tour[-1], 0, "Tour should end at the depot 0")

    def test_visit_each_city_once(self):
        self.assertEqual(sorted(self.tour[1:-1]), sorted(list(self.cities.keys())[1:]), "Each city must be visited exactly once")

    def test_minimize_longest_travel_distance(self):
        calculated_max_distance = 0
        actual_total_distance = 0
        for i in range(len(self.tour) - 1):
            city1 = self.tour[i]
            city2 = self.tour[i + 1]
            distance = math.sqrt((self.cities[city1][0] - self.cities[city2][0]) ** 2 + 
                                  (self.cities[city1][1] - self.cities[city2][1]) ** 2)
            actual_total_distance += distance
            if distance > calculated_max_distance:
                calculated_max_distance = distance
        
        self.assertAlmostEqual(calculated_max_distance, self.reported_max_distance, delta=0.1, msg="Calculated and reported longest distances do not match")
        self.assertAlmostEqual(actual_total_distance, self.reported_total_distance, delta=0.1, msg="Calculated and reported total distances do not match")

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestTSPSolution('test_tour_starts_and_ends_at_depot'))
    test_suite.addTest(TestTSPSolution('test_visit_each_city_once'))
    test_suite.addTest(TestTSPRetort('test_minimize_longest_travel_distance'))

    result = unittest.TextTestRunner(verbosity=2).run(test_suite)

    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")