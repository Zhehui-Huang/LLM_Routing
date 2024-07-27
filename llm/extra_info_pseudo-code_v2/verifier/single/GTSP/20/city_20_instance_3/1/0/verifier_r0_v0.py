import unittest
import math

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61),
            4: (69, 57), 5: (6, 58), 6: (12, 84), 7: (72, 77),
            8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
            12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47),
            16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
        }
        self.groups = [
            [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15],
            [1, 3, 19], [8, 11, 18]
        ]
        self.solution_tour = [0, 4, 7, 12, 15, 3, 18, 0]
        self.expected_cost = 227.40

    def test_start_and_end_at_depot(self):
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)
    
    def test_visit_one_city_per_group(self):
        visited_groups = [False] * len(self.groups)
        for city in self.solution_tour[1:-1]:  # exclude the depot city at start and end
            for i, group in enumerate(self.groups):
                if city in group:
                    self.assertFalse(visited_groups[i])
                    visited_groups[i] = True
        self.assertTrue(all(visited_groups))

    def test_calculated_cost(self):
        def euclidean_distance(city1, city2):
            return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

        tour_cost = 0
        for i in range(len(self.solution_tour) - 1):
            tour_cost += euclidean_distance(self.cities[self.solution_tour[i]], self.cities[self.solution_tour[i + 1]])
        
        # Checking the cost up to one decimal place
        self.assertAlmostEqual(tour_cost, self.expected_cost, places=1)

unittest.main(argv=[''], verbosity=2, exit=False)