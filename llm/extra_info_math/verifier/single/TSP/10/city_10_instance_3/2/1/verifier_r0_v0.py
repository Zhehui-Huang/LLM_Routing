import math
import unittest

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
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

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour does not start at the depot.")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at the depot.")

    def test_visit_each_city_exactly_once(self):
        from collections import Counter
        city_counts = Counter(self.tour)
        self.assertEqual(city_counts[0], 2, "Depot city should be visited exactly twice (start and end).")
        for city in range(1, len(self.cities)):
            self.assertEqual(city_counts[city], 1, f"City {city} should be visited exactly once.")

    def test_total_travel_cost(self):
        total_cost = 0
        for i in range(len(self.tour) - 1):
            x1, y1 = self.cities[self.tour[i]]
            x2, y2 = self.cities[self.tour[i+1]]
            total_cost += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        self.assertAlmostEqual(total_cost, self.reported_cost, places=5, msg="Reported travel cost does not match computed cost.")

    def test_no_subtours(self):
        from collections import defaultdict
        adj = defaultdict(set)
        for i in range(len(self.tour) - 1):
            adj[self.tour[i]].add(self.tour[i+1])
            adj[self.tour[i+1]].add(self.tour[i])
        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor != prev and not dfs(neighbor, node):
                    return False
            return True
        
        self.assertTrue(dfs(self.tour[0], None), "Subtour detected in the route.")

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_loader = unittest.TestLoader()
    test_suite.addTest(test_loader.loadTestsFromTestCase(TestTSPSolution))
    test_runner = unittest.TextTestRunner()
    result = test