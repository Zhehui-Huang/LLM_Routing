import unittest
import math

class TestKTSPSolution(unittest.TestCase):
    def setUp(self):
        # Given city coordinates
        self.cities = [
            (3, 26),   # Depot city 0
            (85, 72),
            (67, 0),
            (50, 99),
            (61, 89),
            (91, 56),
            (2, 65),
            (38, 68),
            (3, 92),
            (59, 8),
            (30, 88),
            (30, 53),
            (11, 14),
            (52, 49),
            (18, 49),
            (64, 41),
            (28, 49),
            (91, 94),
            (51, 58),
            (30, 48)   # City 19
        ]
        # Proposed solution
        self.tour = [0, 14, 16, 19, 11, 7, 4, 13, 9, 0]
        self.total_travel_cost = 234.25

    def test_start_end_depot(self):
        """ Tour must start and end at the depot city (index 0). """
        self.assertEqual(self.tour[0], 0, "Tour does not start at the depot city.")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at the depot city.")

    def test_tour_length(self):
        """ Tour must include exactly 10 cities (counted with repetition). """
        self.assertEqual(len(self.tour), 10, "Tour does not include exactly 10 cities.")

    def test_total_travel_cost(self):
        """ Calculate and check the provided tour travel cost. """
        computed_cost = 0
        for i in range(len(self.tour) - 1):
            x1, y1 = self.cities[self.tour[i]]
            x2, y2 = self.cities[self.tour[i + 1]]
            computed_cost += math.hypot(x2 - x1, y2 - y1)
        self.assertAlmostEqual(computed_cost, self.total_travel_cost, places=2, "Computed travel cost does not match the provided total.")

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestKTSPSolution))
    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

run_tests()