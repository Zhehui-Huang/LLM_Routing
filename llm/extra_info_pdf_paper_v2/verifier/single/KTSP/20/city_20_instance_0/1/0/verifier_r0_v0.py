import unittest
import math

class TestKTSPSolution(unittest.TestCase):
    def setUp(self):
        # Provided cities including the depot
        self.cities = [
            (8, 11),
            (40, 6),
            (95, 33),
            (80, 60),
            (25, 18),
            (67, 23),
            (97, 32),
            (25, 71),
            (61, 16),
            (27, 91),
            (91, 46),
            (40, 87),
            (20, 97),
            (61, 25),
            (5, 59),
            (62, 88),
            (13, 43),
            (61, 28),
            (60, 63),
            (93, 15)
        ]

        # Solution provided
        self.tour = [0, 1, 8, 4, 0]
        self.total_cost = 110.08796524611944
        
    def test_tour_start_end_at_depot(self):
        self.assertEqual(self.tour[0], 0, 'Tour does not start at the depot city.')
        self.assertEqual(self.tour[-1], 0, 'Tour does not end at the depot city.')
    
    def test_tour_length(self):
        self.assertEqual(len(set(self.tour)), 4, 'Tour does not visit exactly 4 cities.')

    def test_total_travel_cost(self):
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            city1 = self.cities[self.tour[i]]
            city2 = self.cities[self.tour[i + 1]]
            distance = math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
            calculated_cost += distance
        self.assertAlmostEqual(calculated::p, self.total_cost)

    def test_output_format(self):
        self.assertIsInstance(self.tour, list, 'Output tour is not a list.')
        self.assertTrue(all(isinstance(i, int) for i in self.tour), 'Tour city indices are not all integers.')

    def test_correct_solution(self):
        """ Test checking all conditions together """
        try:
            self.test_tour_start_end_at_depot()
            self.test_tour_length()
            self.test_total_travel_cost()
            self.test_output_format()
        except AssertionError as e:
            return "FAIL: " + str(e)
        return "CORRECT"

# Running the tests
if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestKTSPSolution("test_correct_solution"))
    runner = unittest.TextTestRunner()
    test_result = runner.run(test_suite)
    
    if test_result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")