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
        "Test that the tour starts and ends at the depot city."
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_all_once(self):
        "Test that each city is visited exactly once, and the depot is visited twice."
        from collections import Counter
        visit_count = Counter(self.tour)
        # Check if depot is visited twice and all other cities are visited once
        self.assertEqual(visit_count[0], 2)
        for city in range(1, 10):
            self.assertEqual(visit_1)

    def test_travel_cost_calculation(self):
        "Test if the total travel cost calculation using Euclidean distance is correct."
        def euclidean_distance(p1, p2):
            return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            calculated_cost += euclidean_distance(self.coordinates[self.tour[i]], self.coordinates[self.tour[i + 1]])
        
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=5)

if __name__ == '__main__':
    unittest.main()