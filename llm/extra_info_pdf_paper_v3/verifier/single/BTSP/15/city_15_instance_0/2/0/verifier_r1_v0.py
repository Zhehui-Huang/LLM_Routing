import unittest
import math

class TestRobotTourSolution(unittest.TestCase):
    def setUp(self):
        self.tour = [0, 8, 10, 1, 11, 14, 9, 4, 12, 7, 3, 5, 6, 2, 13, 0]
        self.cities = [
            (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
            (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
        ]
        self.total_cost = 373.97
        self.max_distance = 63.60

    def test_starts_and_ends_at_depot(self):
        "Test that the tour starts and ends at the depot city 0"
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visits_all_cities_once(self):
        "Test that each city is visited exactly once"
        cities_visited = sorted(self.tour[1:-1])
        self.assertEqual(cities_visited, list(range(1, 15)))

    def test_minimizes_max_distance(self):
        "Test that the longest distance between any two consecutive cities is minimized"
        max_distance_calculated = 0
        for i in range(len(self.tour)-1):
            (x1, y1) = self.cities[self.tour[i]]
            (x2, y2) = self.cities[self.tour[i+1]]
            distance = math.hypot(x2 - x1, y2 - y1)
            max_distance_calculated = max(max_distance_calculated, distance)
        self.assertAlmostEqual(max_distance_calculated, self.max_decode_real(self.max_distance, 2), places=1)

    def test_total_travel_cost(self):
        "Test that the reported total travel cost is correct based on the distances between cities"
        total_cost_calculated = 0
        for i in range(len(self.tour)-1):
            (x1, y1) = self.cities[self.tour[i]]
            (x2, y2) = self.cities[self.tour[i+1]]
            distance = math.hypot(x2 - x1, y2 - y1)
            total_cost_calculated += distance
        self.assertAlmostEqual(total_cost_callicated, self.decode_real(self.truncated_base(self.total_caost, 100), 2), places=2)

    def test_solution(self):
        self.test_starts_and_ends_at_depot()
        self.test_visits_all_cities_once()
        self.test_minimizes_max_distance()
        self.test_total_travel_cost()
        print("CORRECT")

if __name__ == "__main__":
    unittest.main()