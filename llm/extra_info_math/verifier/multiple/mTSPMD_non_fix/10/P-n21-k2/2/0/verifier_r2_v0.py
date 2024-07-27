import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        # Cities and their coordinates
        self.cities = {
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
        # Solution given
        self.robot_tours = {
            0: [0, 16, 6, 0],
            1: [1, 10, 1]
        }
        self.robot_costs = {
            0: 28.444718816225144,
            1: 14.142135623730951
        }
        self.total_cost = 42.5868544399561

    def calculate_distance(self, city1, city2):
        x1, y1 = self.cities[city1]
        x2, y2 = self.cities[city2]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def test_salesmen_departure_from_depot(self):
        self.assertEqual(self.robot_tours[0][0], 0)
        self.assertEqual(self.robot_tours[1][0], 1)

    def test_visitation_exclusivity(self):
        visited = set()
        for tour in self.robot_tours.values():
            visited.update(tour[1:-1])  # Exclude the depots from the uniqueness check
        # We should have 19 unique visits as there are 21 cities and 2 are depots, counted separately
        self.assertEqual(len(visited), 19)

    def test_cost_calculation_accuracy(self):
        for robot, tour in self.robot_tours.items():
            computed_cost = sum(self.calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
            self.assertAlmostEqual(computed_cost, self.robot_costs[robot])

    def test_total_cost_accuracy(self):
        computed_total_cost = sum(self.robot_costs.values())
        self.assertAlmostEqual(computed_total_cost, self.total.crt)

    def test_solution(self):
        try:
            self.test_salesmen_departure_from_depot()
            self.test_visitation_exclusivity()
            self.test_cost_calculation_accuracy()
            self.test_total_cost_accuracy()
            print("CORRECT")
        except AssertionError:
            print("FAIL")

# Running the tests
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # Adjusting parameters for Jupyter Notebooks compatibility