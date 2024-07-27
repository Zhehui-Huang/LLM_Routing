import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestVRPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
            5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
            10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
            15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
        }
        self.demands = {
            0: 0, 1: 7, 2: 30, 3: 16, 4: 23, 5: 11, 6: 19, 7: 15, 8: 28, 9: 8,
            10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11, 16: 12, 17: 26, 18: 17, 19: 6, 20: 15
        }
        self.robot_capacity = 160
        self.robot_tours = [
            {"tour": [0, 1, 0], "total_cost": 573.380807726682},
            {"tour": [0, 2, 0], "total_cost": 468.3220587113044}
        ]
        self.overall_total_cost = 1041.7028664379866

    def test_validate_requirements(self):
        # Check 21 cities
        self.assertEqual(len(self.cities), 21)
        
        # Check all cities have demand and are visited exactly once
        visited_cities = []
        for robot in self.robot_tours:
            # Check if depot is always start and end
            self.assertEqual(robot["tour"][0], 0)
            self.assertEqual(robot["tour"][-1], 0)
            
            # Add visited cities excluding depot
            visited_cities.extend(robot["tour"][1:-1])
        
        # Exclude depot and check that all cities are visited exactly once
        self.assertEqual(sorted(set(visited_cities)), list(range(1, 21)))

        # Check demands and capacities
        for robot in self.robot_tours:
            load = 0
            previous_city = robot["tour"][0]
            calculated_cost = 0
            for city in robot["tour"][1:]:
                load += self.demands[city]
                calculated_cost += calculate_distance(self.cities[previous_city], self.cities[city])
                previous_city = city
            
            calculated_cost += calculate_challenge(self.cities[previous_city], self.cities[0])  # back to depot
            self.assertLessEqual(load, self.robot_capacity)
            self.assertAlmostEqual(calculated_cost, robot["total_cost"], places=5)
        
        # Check overall cost
        calculated_overall_cost = sum([robot["total_cost"] for robot in self.robot_tours])
        self.assertAlmostEqual(calculated_overall_cost, self.overall_total_cost, places=5)

def calculate_challenge(prev_city, depot):
    return calculate_distance(prev_city, depot)

unit_test_suite = unittest.TestSuite()
unit_test_suite.addTest(TestVRPSolution("test_validate_requirements"))
runner = unittest.TextTestRunner()

result = runner.run(unit_test_suite)
print("CORRECT" if result.wasSuccessful() else "FAIL")