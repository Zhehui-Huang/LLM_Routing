import unittest
from math import sqrt

class TestRobotTours(unittest.TestCase):

    def setUp(self):
        # Cities and their coordinates
        self.cities = {
            0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64),
            4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
            8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
            12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33),
            16: (62, 63), 17: (63, 69), 18: (45, 35)
        }

        # Tours provided in the solution
        self.robot_0_tour = [0, 18, 5, 15, 7, 10, 4, 14, 17, 0]
        self.robot_1_tour = [1, 12, 3, 16, 8, 9, 13, 2, 6, 11, 1]
        self.robot_0_cost = 110.30364546391537
        self.robot_1_cost = 131.5750602083226
        self.total_cost = 241.87870567223797

    def test_tour_starts_at_depot_0(self):
        self.assertEqual(self.robot_0_tour[0], 0)
    
    def test_city_visit_once(self):
        all_cities_visited = self.robot_0_tour + self.robot_1_tour
        unique_cities = set(all_cities_visited)
        self.assertEqual(len(all_cities_visited) - 2, len(unique_cities))  # Subtract 2 for repeat of depots

    def test_no_return_requirement_met(self):
        self.assertNotEqual(self.robot_0_tour[-1], 0, "Robot 0 should not necessarily end at depot 0")
        self.assertNotEqual(self.robot_1_tour[-1], 1, "Robot 1 should not necessarily end at depot 1")

    def test_costs(self):
        def calculate_cost(tour):
            cost = 0
            for i in range(1, len(tour)):
                x1, y1 = self.cities[tour[i-1]]
                x2, y2 = self.cities[tour[i]]
                cost += sqrt((x2 - x1)**2 + (y2 - y1)**2)
            return cost
        
        calculated_cost_0 = calculate_cost(self.robot_0_tour)
        calculated_cost_1 = calculate_cost(self.robot_1_tour)
        
        self.assertAlmostEqual(calculated_cost_0, self.robot_0_cost, places=5, msg=f"Cost for robot 0 should be close to {self.robot_0_cost}")
        self.assertAlmostEqual(calculated_cost_1, self.robot_1_cost, places=5, msg=f"Cost for robot 1 should be close to {self.robot_1_cost}")

        total_calculated_cost = calculated_cost_0 + calculated_cost_1
        self.assertAlmostEqual(total_calculated_cost, self.total_cost, places=5, msg="Total cost should match calculated total cost")

# Run the test
suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTours)
unittest.TextTestRunner().run(suite)