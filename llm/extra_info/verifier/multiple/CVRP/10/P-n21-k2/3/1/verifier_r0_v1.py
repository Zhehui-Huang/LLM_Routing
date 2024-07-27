import unittest
import math

class TestVRPSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = {
            0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
            4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
            8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
            12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
            16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
            20: (45, 35)
        }
        self.demand = {
            0: 0, 1: 7, 2: 30, 3: 16, 4: 23, 5: 11, 6: 19, 7: 15, 8: 28, 9: 8,
            10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11, 16: 12, 17: 26,
            18: 17, 19: 6, 20: 15
        }
        self.robot_tours = {
            0: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
            1: [0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0]
        }
        self.robot_capacity = 160
        self.claimed_cost = {
            0: 187.81, 1: 287.43
        }
        self.total_claimed_cost = 475.24

    def runTest(self):
        try:
            # Test each tour starts and ends at the depot
            for tour in self.robot_tours.values():
                self.assertEqual(tour[0], 0, "Tour does not start at depot")
                self.assertEqual(tour[-1], 0, "Tour does not end at depot")

            # Test capacity constraints
            for tour in self.robot_tours.values():
                total_demand = sum(self.demand[city] for city in tour if city != 0)
                self.assertLessEqual(total_demand, self.robot_capacity, "Capacity exceeded")

            # Test unique city delivery
            all_cities = sum(self.robot_tours.values(), [])
            non_depot_cities = [city for city in all_cities if city != 0]
            self.assertEqual(len(non_depot_cities), len(set(non_depot_cities)), "City delivered more than once")

            # Test travel cost calculation
            def euclidean_distance(c1, c2):
                return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)
            total_calculated_cost = 0
            for i, tour in self.robot_tours.items():
                cost = sum(euclidean_distance(self.coordinates[tour[j]], self.coordinates[tour[j + 1]]) for j in range(len(tour) - 1))
                self.assertAlmostEqual(cost, self.claimed_cost[i], places=2, msg="Incorrect travel cost for robot")
                total_calculated_cost += cost
            self.assertAlmostEqual(total_calculated_cost, self.total_claimed_cost, places=2, msg="Incorrect total travel cost")
            print("CORRECT")
        except AssertionError as e:
            print("FAIL:", e)

# Execute the test
test_case = TestVRPSolution()
test_case.runTest()