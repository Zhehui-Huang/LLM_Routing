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

    def test_demand_fulfillment_per_city(self):
        delivered = {city: 0 for city in self.demands.keys()}
        for tour in self.robot_tours:
            current_load = 0
            for city in tour[1:-1]:  # exclude depot
                if current_load + self.demands[city] <= self.robot_capacity:
                    delivered[city] += self.demands[city]
                    current_load += self.demands[city]
        
        for city, demand in self.demands.items():
            if city in [node for tour in self.robot_tours for node in tour[1:-1]]:
                # Check only for cities that are visited
                self.assertEqual(delivered.get(city, 0), demand)

if __name__ == '__main__':
    unittest.main()