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

    def test_each_city_visited_once(self):
        visited_cities = set()
        for tour in self.robot_tours.values():
            visited_cities.update(tour)
        # Remove depot 0 from set since it's expected to be in every tour
        visited_cities.remove(0)
        self.assertEqual(len(visited_cities), 20)  # Total should be 20 unique cities

    def test_correct_tours_format(self):
        for tour in self.robot_tours.values():
            self.assertTrue(tour[0] == tour[-1] == 0)

    def test_minimum_maximum_cost(self):
        calculated_costs = []
        for robot, tour in self.robot_tours.items():
            total_cost = sum(
                sqrt((self.coordinates[tour[i]][0] - self.coordinates[tour[i+1]][0])**2 +
                     (self.coordinates[tour[i]][1] - self.coordinates[tour[i+1]][1])**2)
                for i in range(len(tour) - 1)
            )
            calculated_costs.append(total_cost)
            self.assertAlmostEqual(total_cost, self.expected_costs[robot])
        self.assertAlmostEqual(max(calculatedrops(self.expected_costs.values()), max(calculated_costs))

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTourSolution)
    result = unittest.TextTestRunner().run(suite)
    return result.wasSuccessful()

# Output result based on the tests
print("CORRECT" if run_tests() else "FAIL")