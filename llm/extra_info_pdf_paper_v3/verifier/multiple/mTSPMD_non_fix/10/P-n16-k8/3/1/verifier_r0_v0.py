import unittest
from math import sqrt

class TestRobotTourSolution(unittest.TestCase):
    def test_robot_tours(self):
        # Positions of cities
        cities = {
            0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
            4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
            8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
            12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
        }

        # Provided robot tours and costs
        robot_tours = {
            0: ([0, 1, 0], 13.892443989449804),
            1: ([0, 2, 0], 21.02379604162864),
            2: ([0, 5, 0], 23.08679276123039),
            3: ([0, 7, 0], 22.02271554554524),
            4: ([0, 10, 0], 20.808652046684813),
            5: ([0, 4, 0], 22.02271554554524),
            6: ([0, 11, 0], 28.160255680657446),
            7: ([0, 6, 0], 12.041594578792296),
        }

        overall_total_cost = 163.05896618953386
        visited_cities = set()
        calculated_total_cost = 0

        for robot, (tour, stated_cost) in robot_tours.items():
            self.assertEqual(tour[0], 0, "Each robot must start from city 0")
            self.assertEqual(tour[-1], 0, "Each robot must end at city 0")
            # Check the path cost
            path_cost = sum(sqrt((cities[tour[i]][0] - cities[tour[i + 1]][0]) ** 2 + (cities[tour[i]][1] - cities[tour[i + 1]][1]) ** 2) for i in range(len(tour) - 1))
            self.assertAlmostEqual(path_cost, stated_cost, places=5, msg="Path cost must match the stated cost")
            visited_cities.update(tour)
            calculated_total_cost += stated_cost

        self.assertEqual(len(visited_cities), 12, "All city should be visited exactly once considering all robots")
        self.assertAlmostEqual(calculated_total_cost, overall_total_cost, places=5, msg="Calculated overall cost should match the stated overall total travel cost")

# Run the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)