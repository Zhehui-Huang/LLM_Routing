import math
from unittest import TestCase, main

# Coordinates of cities
coordinates = {
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
}

def calculate_travel_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        x1, y1 = coordinates[tour[i - 1]]
        x2, y2 = coordinates[tour[i]]
        cost += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return cost

class TestTSPSolution(TestCase):
    def setUp(self):
        self.robot0_tour = [0, 10, 19, 8, 2, 17, 6, 20, 5, 14, 0]
        self.robot1_tour = [0, 7, 4, 11, 3, 18, 9, 13, 12, 15, 0]
        self.solution_cost = {
            "robot0": 163.52680536148745,
            "robot1": 182.87611885521116,
            "total": 346.4029242166986
        }
    
    def test_all_cities_visited_exactly_once(self):
        all_cities_visited = set(self.robot0_tour + self.robot1_tour)
        # Include all cities from 0 to 20 except the first depot (0) duplicated for start and end
        expected_cities = set(range(21))
        self.assertEqual(all_cities_visited, expected_cities)
    
    def test_tours_start_at_depot_city_0_and_end_at_city(self):
        self.assertEqual(self.robot0_tour[0], 0)
        self.assertEqual(self.robot0_tour[-1], 0)
        self.assertEqual(self.robot1_tour[0], 0)
        self.assertEqual(self.robot1_tour[-1], 0)

    def test_total_travel_cost(self):
        calculated_robot0_cost = calculate_travel_cost(self.robot0_tour)
        calculated_robot1_cost = calculate_travelill_cost(self.robot1_tour)

        self.assertAlmostEqual(calculated_robot0_cost, self.solution_cost["robot0"], places=4)
        self.assertAlmostEqual(calculated_robot1_cost, self.solution_cost["robot1"], places=4)
        self.assertAlmostEqual(calculated_robot0_cost + calculated_robot1_cost, self.solution_cost["total"], places=4)

if __name__ == '__main__':
    test_results = main(exit=False)
    if test_results.result.wasSuccessful():
        print("CORRECT")
    else:
         print("FAIL")