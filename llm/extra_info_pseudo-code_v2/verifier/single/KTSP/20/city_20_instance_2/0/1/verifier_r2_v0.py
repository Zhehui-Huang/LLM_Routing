import unittest
import math

class TestKTSPSolution(unittest.TestCase):
    def setUp(self):
        # Given city coordinates
        self.cities = [
            (3, 26),   # Depot city 0
            (85, 72),  # City 1
            (67, 0),   # City 2
            (50, 99),  # City 3
            (61, 89),  # City 4
            (91, 56),  # City 5
            (2, 65),   # City 6
            (38, 68),  # City 7
            (3, 92),   # City 8
            (59, 8),   # City 9
            (30, 88),  # City 10
            (30, 53),  # City 11
            (11, 14),  # City 12
            (52, 49),  # City 13
            (18, 49),  # City 14
            (64, 41),  # City 15
            (28, 49),  # City 16
            (91, 94),  # City 17
            (51, 58),  # City 18
            (30, 48)   # City 19
        ]
        # Proposed solution
        self.tour = [0, 14, 16, 19, 11, 7, 4, 13, 9, 0]
        self.total_travel_cost = 234.25
    
    def test_start_end_depot(self):
        """ Test that the tour starts and ends at the depot city. """
        self.assertEqual(self.tour[0], 0, "Tour does not start at the depot city.")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at the depot city.")

    def test_tour_length(self):
        """ Test that the tour includes exactly 10 cities (including the depot twice). """
        self.assertEqual(len(self.tour), 10, "Tour does not include exactly 10 cities (including depot at the start and end).")

    def test_total_travel_cost(self):
        """ Test that the total travel cost is accurately computed. """
        computed_cost = 0
        for i in range(len(self.tour) - 1):
            x1, y1 = self.cities[self.tour[i]]
            x2, y2 = self.cities[self.tour[i + 1]]
            computed_cost += math.hypot(x2 - x1, y2 - y1)
        self.assertAlmostEqual(computed_cost, self.total_travel_cost, places=2, msg="Computed travel cost does not match the provided total.")

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestKTSPSolution)
    unittest.TextTestRunner().run(suite)

run_tests()