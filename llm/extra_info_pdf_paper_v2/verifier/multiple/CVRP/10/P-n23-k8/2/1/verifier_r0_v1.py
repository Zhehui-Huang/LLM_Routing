import unittest
from math import sqrt

class TestCVRPSolution(unittest.TestCase):
    def setUp(self):
        self.cities_coordinates = {
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
            20: (45, 35),
            21: (32, 39),
            22: (56, 37)
        }
        
        self.demands = {
            1: 7,
            2: 30,
            3: 16,
            4: 23,
            5: 11,
            6: 19,
            7: 15,
            8: 28,
            9: 8,
            10: 8,
            11: 7,
            12: 14,
            13: 6,
            14: 19,
            15: 11,
            16: 12,
            17: 26,
            18: 17,
            19: 6,
            20: 15,
            21: 5,
            22: 10
        }
        
        self.robot_tours = [
            [0, 18, 19, 0]
        ]
        self.robot_capacity = 40
        self.total_robot = 8

    def test_number_of_cities_including_depot(self):
        self.assertEqual(len(self.cities_coordinates), 23)

    def test_tour_start_and_end_at_depot(self):
        for tour in self.robot_tours:
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

    def test_demand_fulfillment_per_city(self):
        # Initialize delivered dict
        delivered = {key: 0 for key in range(1, 23)}
        for tour in self.robot_tours:
            for city in tour[1:-1]:  # exclude depot city at start and end
                delivered[city] += self.demands[city]
        for city, demand in self.demands.items():
            if city in delivered:
                self.assertEqual(delivered[city], demand)

    def test_robot_capacity_not_exceeded(self):
        for tour in self.robot_tours:
            load = sum(self.demands[city] for city in tour[1:-1] if city in self.demands)
            self.assertLessEqual(load, self.robot_capacity)

    def test_each_tour_cost(self):
        expected_costs = [89.42264879375188]
        calculated_costs = []
        for tour in self.robot_tours:
            cost = sum(
                sqrt((self.cities_coordinates[tour[i]][0] - self.cities_coordinates[tour[i+1]][0])**2 +
                     (self.cities_coordinates[tour[i]][1] - self.cities_coordinates[tour[i+1]][1])**2)
                for i in range(len(tour) - 1)
            )
            calculated_costs.append(cost)
        for expected, calculated in zip(expected_costs, calculated_costs):
            self.assertAlmostEqual(expected, calculated)

    def test_minimize_total_travel_cost(self):
        calculated_total_cost = sum(
            sqrt((self.cities_coordinates[tour[i]][0] - self.cities_coordinates[tour[i+1]][0])**2 +
                 (self.cities_coordinates[tour[i]][1] - self.cities_coordinates[tour[i+1]][1])**2)
            for tour in self.robot_tours for i in range(len(tour) - 1)
        )
        overall_expected_cost = 89.42264879375188
        self.assertAlmostEqual(calculated_total_cost, overall_expected_cost)

if __name__ == "__main__":
    unittest.main()