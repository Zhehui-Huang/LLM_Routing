import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
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
        self.tour = [0, 7, 1, 4, 2, 5, 6, 9, 3, 8, 0]
        self.reported_cost = 294.17253892411236

    def test_tour_start_end_at_depot(self):
        """Verifies that the tour starts and ends at the depot."""
        self.assertEqual(self.tour[0], 0, "Tour does not start at the depot.")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at the depot.")

    def test_visit_each_city_once(self):
        """Ensures each city is visited exactly once."""
        for city in set(self.tour[1:-1]):
            self.assertEqual(self.tour.count(city), 1, f"City {city} is not visited exactly once.")

    def test_total_travel_cost(self):
        """Calculates and compares the total travel cost of the tour."""
        total_cost = 0
        for i in range(len(self.tour) - 1):
            x1, y1 = self.cities[self.tour[i]]
            x2, y2 = self.cities[self.tour[i + 1]]
            total_cost += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.assertAlmostEqual(total_cost, self.reported_cost, places=5, msg="Calculated cost does not match the reported cost.")

    def test_no_subtours(self):
        """Checks if the tour constitutes a single loop without subtours."""
        # Check if there is a continuous path visiting all cities exactly once
        visited = [False] * len(self.cities)
        current = 0
        for next_city in self.tour[1:]:
            visited[current] = True
            current = next_city
            if visited[current] and current != 0:
                self.fail("Subtour detected because of revisiting a city before the tour completes.")
        self.assertTrue(all(visited), "Not all cities were checked, indicating incomplete tour traversal.")

if __name__ == "__main__":
    unittest.main()