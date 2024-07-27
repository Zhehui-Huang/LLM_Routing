import unittest
from math import sqrt

class TestRobotTourSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = {
            0: (30, 40),
            1: (37, 52),
            2: (49, 49),
            3: (52, 64),
            4: (31, 62),
            5: (52, 33),
            6: (42, 41),
            7: (52, 41),
            8: (57, 58),
            9: (62, 42),
            10: (42, 57),
            11: (27, 68),
            12: (43, 67),
            13: (58, 48),
            14: (58, 27),
            15: (37, 69),
            16: (38, 46),
            17: (61, 33),
            18: (62, 63),
            19: (63, 69),
            20: (45, 35)
        }
        self.robot_tours = {
            0: [0, 1, 3, 6, 7, 8, 10, 14, 15, 17, 18, 0],
            1: [0, 2, 4, 5, 9, 11, 12, 13, 16, 19, 20, 0]
        }
        self.expected_costs = {
            0: 294.5838564979063,
            1: 284.6776492780507
        }
        self.max_cost = max(self.expected_costs.values())

    def test_each_city_visited_once(self):
        visit_count = {key: 0 for key in self.coordinates.keys()}
        for tour in self.robot_tours.values():
            for city in tour:
                if city in visit_count:
                    visit_count[city] += 1
        # Exclude the depot city's double count, once for start and end for tours
        visit_count[0] = 1
        for count in visit_count.values():
            self.assertEqual(count, 1)

    def test_correct_tours_format(self):
        for tour in self.robot_tours.values():
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

    def test_minimum_maximum_cost(self):
        self.assertAlmostEqual(max(self.expected_costs.values()), self.max_cost)

    def test_travel_cost_calculation(self):
        def calculate_distance(p1, p2):
            return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

        for robot, tour in self.robot_tours.items():
            total_cost = sum(calculate_distance(self.coordinates[tour[i]], self.coordinates[tour[i+1]]) for i in range(len(tour)-1))
            self.assertAlmostEqual(total_cost, self.expected_costs[robot])

unittest.main(argv=[''], exit=False)