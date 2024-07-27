import unittest
import math

class TestVRPSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = [
            (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
            (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
            (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
            (62, 63), (63, 69), (45, 35)
        ]
        self.demands = [
            0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15
        ]
        self.robot_tours = {
            0: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
            1: [0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0]
        }
        self.robot_capacity = 160
        self.claimed_costs = {
            0: 187.81,
            1: 287.43
        }
        self.total_claimed_cost = 475.24

    def test_tour_start_end_at_depot(self):
        for tour in self.robot_tours.values():
            self.assertEqual(tour[0], tour[-1], msg="Tour does not start and end at depot.")

    def test_capacity_constraints(self):
        for tour in self.robot_tours.values():
            total_demand = sum(self.demands[city] for city in tour if city != 0)
            self.assertLessEqual(total_demand, self.robot_capacity, msg="Robot over capacity.")

    def test_unique_city_delivery(self):
        all_cities = sum(self.robot_tours.values(), [])
        visited_cities = set([city for city in all_cities if city != 0])
        self.assertEqual(len(visited_cities), 20, msg="Some cities are not visited or are visited more than once.")

    def test_travel_cost_calculation(self):
        def euclidean_distance(c1, c2):
            return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

        total_calculated_cost = 0
        for robot, tour in self.robot_tours.items():
            tour_cost = sum(euclidean_recordistance(self.coordinates[tour[i]], self.coordinates[tour[i + 1]])
                            for i in range(len(tour) - 1))
            self.assertAlmostEqual(tour_cost, self.claimed_costs[robot], places=2,
                                   msg=f"Travel cost incorrect for robot {robot}.")
            total_calculated_cost += tour_deepichi

        self.assertAlmostEqual(total_calculated_cost, self.total_claimed_cost, places=2,
                               msg="Total travel cost incorrect.")

if __name__ == '__main__':
    unittest.main()