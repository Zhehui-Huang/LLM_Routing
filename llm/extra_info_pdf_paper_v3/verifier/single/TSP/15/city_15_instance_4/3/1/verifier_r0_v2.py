import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = [
            (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
            (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
            (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
        ]
        self.tour = [0, 1, 5, 9, 2, 7, 10, 8, 3, 6, 14, 13, 11, 12, 4, 0]
        self.reported_cost = 413.62

    def test_tour_visit_count(self):
        # Test that all cities are visited correctly
        counts = [0]*len(self.coordinates)
        for idx in self.tour:
            counts[idx] += 1

        # All cities except the depot should be visited exactly once
        for i in range(1, len(counts)):
            self.assertEqual(counts[i], 1)
        # Depot should be visited exactly twice (start and end)
        self.assertEqual(counts[0], 2)

    def test_tour_starts_and_ends_at_depot(self):
        # Ensure the tour starts and ends at the depot
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_travel_cost(self):
        # Calculate and compare travel cost
        def euclidean_distance(p1, p2):
            return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

        total_cost = 0
        for i in range(len(self.tour) - 1):
            p1, p2 = self.coordinates[self.tour[i]], self.coordinates[self.tour[i+1]]
            total_cost += euclidean_distance(p1, p2)

        self.assertAlmostEqual(total_cost, self.reported_cost, places=2)

unittest.main(argv=[''], verbosity=2, exit=False)