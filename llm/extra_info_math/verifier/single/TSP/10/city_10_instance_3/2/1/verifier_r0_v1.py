import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        # City coordinates
        self.cities = [
            (84, 67),  # City 0 (Depot)
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
        self.tour = [0, 7, 1, 4, 2, 5, 6, 9, 3, 8, 0]
        self.reported_cost = 294.17253892411236

    def test_tour_start_end_at_depot(self):
        """Check if the tour starts and ends at the depot"""
        self.assertEqual(self.tour[0], 0, "Tour should start at depot.")
        self.assertEqual(self.tour[-1], 0, "Tour should end at depot.")

    def test_visit_each_city_once(self):
        """Check if each city is visited exactly once"""
        visited = set(self.tour)  # Cities that are visited
        self.assertEqual(len(visited), len(self.cities), "Some cities are not visited or visited more than once.")

    def test_total_travel_cost_accuracy(self):
        """Check the total travel cost calculation accuracy"""
        total_cost = 0
        for i in range(len(self.tour) - 1):
            x1, y1 = self.cities[self.tour[i]]
            x2, y2 = self.cities[self.tour[i + 1]]
            total_cost += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.assertAlmostEqual(total_cost, self.reported_cost, places=5, "Calculated cost does not match the reported cost.")

    def test_no_subtours(self):
        """Ensure there are no subtours"""
        visited = [False] * len(self.cities)
        stack = [self.tour[0]]
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                for i in range(1, len(self.tour) - 1):
                    if self.tour[i] == node:
                        stack.append(self.tour[i + 1])
        self.assertTrue(all(visited), "Not all cities were visited, indicating possible subtours.")

if __name__ == '__main__':
    unittest.main()