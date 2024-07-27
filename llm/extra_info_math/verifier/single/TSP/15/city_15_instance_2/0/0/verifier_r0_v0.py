import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (54, 87),  # Depot city 0
            (21, 84),  # City 1
            (69, 84),  # City 2
            (53, 40),  # City 3
            (54, 42),  # City 4
            (36, 30),  # City 5
            (52, 82),  # City 6
            (93, 44),  # City 7
            (21, 78),  # City 8
            (68, 14),  # City 9
            (51, 28),  # City 10
            (44, 79),  # City 11
            (56, 58),  # City 12
            (72, 43),  # City 13
            (6, 99)   # City 14
        ]
        self.tour = [0, 2, 7, 13, 9, 10, 5, 3, 4, 12, 8, 1, 14, 11, 6, 0]
        self.expected_cost = 311.87764180786695

    def test_tour_start_end_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour should start at depot city 0.")
        self.assertEqual(self.tour[-1], 0, "Tour should end at depot city 0.")

    def test_visit_all_cities_once(self):
        unique_cities = set(self.tour)
        self.assertEqual(len(unique_cities), 15, "Should visit all 15 distinct cities including depot exactly once.")
        self.assertEqual(len(self.tour), 16, "Depot should appear exactly twice, total 16 stops.")

    def test_exact_match_of_cities_visited(self):
        all_cities = set(range(15))
        visited_cities = set(self.tour)
        self.assertEqual(visited_cities, all_cities, "Visited cities do not match the list of all cities.")
        
    def test_travel_cost_calculation(self):
        def calculate_euclidean_distance(p1, p2):
            return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

        total_cost = 0
        for i in range(len(self.tour) - 1):
            total_cost += calculate_euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])

        self.assertAlmostEqual(total_cost, self.expected_cost, places=5, msg="Computed tour cost does not match expected cost.")

unittest.main(argv=[''], exit=False)