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
        self.reported_total_cost = 185.24224625522046

    def test_solution_correctness(self):
        all_cities = sum(self.tours.values(), [])
        all_cities_without_depots_return = [city for city in all_cities if city != all_cities[0]]

        starts_ends_correct = all(self.tours[robot][0] == self.tours[robot][-1] for robot in self.tours)
        all_unique_cities = len(set(all_cities_without_depots_return)) == 22  # 23 cities including depots - 1 because depots are re-visited
        correct_visit_count = len(all_cities_without_depots_return) == 22
        all_conditions = starts_ends_correct and all_unique_cities and correct_visit_count

        total_calculated_cost = 0
        for robot_id, tour in self.tours.items():
            robot_cost = sum(sqrt((self.city_coords[tour[i]][0] - self.city_coords[tour[i + 1]][0])**2 +
                                  (self.city_coords[tour[i]][1] - self.city_coords[tour[i + 1]][1])**2)
                             for i in range(len(tour) - 1))
            self.assertAlmostEqual(robot_cost, self.reported_costs[robot_id], places=5)
            total_calculated_cost += robot_cost

        total_cost_correct = abs(total_calculated_cost - self.reported_total_cost) < 0.001

        if all_conditions and total_cost_correct:
            print("CORRECT")
        else:
            print("FAIL")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)