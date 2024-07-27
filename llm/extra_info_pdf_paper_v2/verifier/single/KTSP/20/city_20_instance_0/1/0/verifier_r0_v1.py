import unittest
import math

class TestKTSPSolution(unittest.TestCase):
    def setUp(self):
        # Provided cities including the depot
        self.cities = [
            (8, 11),   # Depot
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
        self.assertEqual(len(self.tour), 5, 'Tour does not have exactly 5 vertices including the return to the depot.')
        self.assertEqual(len(set(self.tour) - {0}), 3, 'Tour does not visit exactly 3 unique cities other than the depot.')

    def test_total_travel_cost(self):
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            city1 = self.cities[self.tour[i]]
            city2 = self.cities[self.tour[i + 1]]
            distance = math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
            calculated_cost += distance
        self.assertAlmostEqual(calculated_cost, self.total_cost, places=5, msg='Calculated travel cost does not match provided total cost.')

    def test_output_format(self):
        self.assertIsInstance(self.tour, list, 'Output tour is not a list.')
        self.assertTrue(all(isinstance(i, int) for i in self.tour), 'Tour city indices are not all integers.')

# Running the tests
if __name__ == '__main__':
    unittest.main()