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
        self.total_cost = 185.24224625522046

    def test_solution(self):
        all_cities_visited = sum(self.tours.values(), [])
        unique_cities = set(all_cities_visited)
        all_visits_correct = len(all_cities_visited) == len(self.city_coords) + len(self.tours)# Each city + reentry at depot
        starts_and_ends_correct = all(self.tours[robot_id][0] == self.tours[robot_id][-1] for robot_id, _ in self.tours.items())
        calculated_total_cost = 0

        for robot_id, tour in self.tours.items():
            total_cost = 0
            for i in range(len(tour) - 1):
                start = self.city_coords[tour[i]]
                end = self.city_coords[tour[i + 1]]
                dist = sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
                total_cost += dist
            calculated_total_cost += total_cost
            self.assertAlmostEqual(total_cost, self.reported_costs[robot_id], places=5)

        correct_total_cost = abs(calculated_total_cost - self.total_cost) < 0.0001

        # Assert condition for solution being correct
        if all_visits_correct and starts_and_ends_correct and correct_total_...
            print("CORRECT")
        else:
            print("FAIL")


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)