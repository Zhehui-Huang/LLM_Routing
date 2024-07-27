import unittest
from math import sqrt

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        self.tours = [
            [0, 3, 8, 0], [0, 5, 14, 0], [0, 2, 6, 0], [0, 13, 9, 0],
            [0, 1, 10, 0], [0, 15, 11, 0], [0, 4, 12, 0], [0, 7, 0]
        ]
        self.city_coordinates = {
            0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
            4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
            8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
            12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
        }
        self.reported_costs = [72.82, 62.44, 43.70, 68.39, 41.77, 68.04, 64.99, 44.05]
        self.reported_total_cost = 466.20
    
    def euclidean_distance(self, c1, c2):
        return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

    def test_start_and_end_at_depot(self):
        for tour in self.tours:
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

    def test_visit_all_cities_exactly_once(self):
        visited = sum((tour[1:-1] for tour in self.tours), [])
        self.assertEqual(len(set(visited)), 15)
        self.assertEqual(set(visited), set(range(1, 16)))

    def test_tour_costs(self):
        calculated_costs = []
        for tour in self.tours:
            cost = sum(self.euclidean_distance(self.city_coordinates[tour[i]], self.city_coordinates[tour[i+1]]) for i in range(len(tour)-1))
            calculated_costs.append(round(cost, 2))
        for reported, calculated in zip(self.reported_costs, calculated_costs):
            self.assertAlmostEqual(reported, calculated, places=2)
    
    def test_total_cost(self):
        total_cost = sum(self.reported_costs)
        self.assertAlmostEqual(self.reported_total_cost, total_cost, places=2)

if __name__ == '__main__':
    unittest.main()