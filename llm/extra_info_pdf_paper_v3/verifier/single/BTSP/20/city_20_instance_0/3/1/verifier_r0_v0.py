import unittest
from math import sqrt

def calculate_distance(city1, city2):
    return sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        # Cities coordinates index corresponds to the city number
        self.cities = [
            (8, 11), # City 0 - Depot
            (40, 6), # City 1
            (95, 33), # City 2
            (80, 60), # City 3
            (25, 18), # City 4
            (67, 23), # City 5
            (97, 32), # City 6
            (25, 71), # City 7
            (61, 16), # City 8
            (27, 91), # City 9
            (91, 46), # City 10
            (40, 87), # City 11
            (20, 97), # City 12
            (61, 25), # City 13
            (5, 59), # City 14
            (62, 88), # City 15
            (13, 43), # City 16
            (61, 28), # City 17
            (60, 63), # City 18
            (93, 15)  # City 19
        ]
        # Given tour
        self.tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
        # Maximum distance between consecutive cities in the tour reported
        self.reported_max_distance = 32.39
    
    def test_begin_end_at_depot(self):
        # Requirement 1: Starts and ends at depot
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_each_city_once(self):
        # Requirement 2: Each city visited exactly once
        visited = set(self.tour[1:-1])
        self.assertEqual(len(visited), 19)
        self.assertSetEqual(visited, set(range(1, 20)))

    def test_max_distance_check(self):
        max_distance = 0
        for i in range(len(self.tour) - 1):
            distance = calculate_distance(self.cities[self.tour[i]], self.cities[self.tour[i+1]])
            if distance > max_distance:
                max_distance = distance
        self.assertAlmostEqual(max_distance, self.reported_max_distance, places=2)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)