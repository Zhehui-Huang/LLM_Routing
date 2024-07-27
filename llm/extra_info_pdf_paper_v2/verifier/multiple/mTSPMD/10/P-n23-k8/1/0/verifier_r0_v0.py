import unittest
from math import sqrt

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        self.tours = {
            0: [0, 21, 0],
            1: [1, 16, 10, 1],
            2: [2, 13, 2],
            3: [3, 8, 18, 19, 12, 3],
            4: [4, 11, 15, 4],
            5: [5, 22, 17, 14, 5],
            6: [6, 20, 6],
            7: [7, 9, 7]
        }
        self.depot_coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41)]
        self.city_coords = [
            (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
            (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
            (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
            (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
        ]
        self.reported_costs = [
            4.47213595499958, 24.85853025288332, 18.110770276274835,
            50.55066424081727, 26.480522629341756, 27.253463793663165,
            13.416407864998739, 20.09975124224178
        ]

    def test_starts_and_ends_at_depot(self):
        for robot_id, tour in self.tours.items():
            self.assertEqual(tour[0], tour[-1], f"Robot {robot_id} does not start and end at the same depot.")

    def test_visit_all_cities_exactly_once(self):
        all_cities_visited = sum(self.tours.values(), [])
        unique_cities = set(all_cities_visited)
        self.assertEqual(len(all_cities_visited), len(unique_cities) + len(self.tours), "Cities visited incorrectly or not exactly once.")

    def test_correct_travel_cost(self):
        calculated_costs = []
        for robot_id, tour in self.tours.items():
            total_cost = 0
            for i in range(len(tour) - 1):
                start = self.city_coords[tour[i]]
                end = self.city_coords[tour[i + 1]]
                dist = sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                total_cost += dist
            calculated_costs.append(total_cost)
        for reported_cost, calculated_cost in zip(self.reported_costs, calculated_costs):
            self.assertAlmostEqual(reported_cost, calculated_cost, places=6)

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)