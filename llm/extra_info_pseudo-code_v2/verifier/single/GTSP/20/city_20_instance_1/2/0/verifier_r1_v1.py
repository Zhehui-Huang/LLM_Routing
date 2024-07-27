import unittest
from math import sqrt

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 
            5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 
            10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
            15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
        }
        self.groups = {
            0: [5, 6, 7, 11, 17],
            1: [1, 4, 8, 13, 16],
            2: [2, 10, 15, 18, 19],
            3: [3, 9, 12, 14]
        }
        self.solution_tour = [0, 11, 15, 1, 12, 0]
        self.solution_cost = 258.05

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)

    def test_tour_visits_one_city_from_each_group(self):
        visited = set(self.solution_tour[1:-1])  # ignore starting and ending depot
        for group_id, group_cities in self.groups.items():
            self.assertTrue(any(city in group_cities for city in visited))

    def test_calculate_euclidean_distance(self):
        def euclidean_distance(city1, city2):
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            return sqrt((x2 - x1)**2 + (y2 - y1)**2)

        calculated_cost = 0
        for i in range(len(self.solution_tour) - 1):
            calculated_cost += euclidean_distance(self.solution_tour[i], self.solution_tour[i+1])

        self.assertAlmostEqual(calculated, self.solution_cost, places=2)

if __name__ == "__main__":
    unittest.main()