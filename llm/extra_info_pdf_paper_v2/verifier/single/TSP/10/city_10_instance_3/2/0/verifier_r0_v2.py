import unittest
from math import sqrt

class TestRobotTour(unittest.TestCase):

    def setUp(self):
        self.coordinates = [
            (84, 67),  # Depot city 0
            (74, 40),  # City 1
            (71, 13),  # City 2
            (74, 82),  # City 3
            (97, 28),  # City 4
            (0, 31),   # City 5
            (8, 62),   # City 6
            (74, 56),  # City 7
            (85, 71),  # City 8
            (6, 76)    # City 9
        ]
        self.tour = [0, 8, 3, 7, 1, 4, 2, 5, 6, 9, 0]
        self.reported_cost = 315.5597914831042

    def test_start_end_at_depot(self):
        # Test that the tour starts and ends at the depot city 0.
        self.assertEqual(self.tour[0], 0, "Tour should start at depot.")
        self.assertEqual(self.tour[-1], 0, "Tour should end at depot.")

    def test_visit_all_once(self):
        # Test that each city is visited exactly once, except the depot which is visited twice.
        counts = {x: self.tour.count(x) for x in self.tour}
        expected_counts = {x: 1 for x in range(1, 10)}  # Cities 1 to 9 should be visited once.
        expected_counts[0] = 2  # Depot city 0 should be visited twice.
        self.assertEqual(counts, expected_counts, "Each city should be visited the correct number of times.")

    def test_travel_cost_calculation(self):
        # Test calculation of the total travel cost using Euclidean distance.
        def euclidean(p1, p2):
            return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

        actual_cost = 0
        for i in range(len(self.tour) - 1):
            p1 = self.coordinates[self.tour[i]]
            p2 = self.coordinates[self.tour[i + 1]]
            actual_cost += euclidean(p1, p2)

        self.assertAlmostEqual(actual_cost, self.reported_cost, places=5, msg="Reported travel cost should match calculated cost.")

if __name__ == '__main__':
    unittest.main()