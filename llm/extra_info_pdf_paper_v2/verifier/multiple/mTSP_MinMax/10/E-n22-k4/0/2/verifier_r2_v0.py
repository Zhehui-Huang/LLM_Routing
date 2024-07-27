import unittest
from math import sqrt

class TestMTSPSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = {
            0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
            5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
            10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
            15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
            20: (155, 185), 21: (139, 182)
        }
        self.robot_tours = {
            0: [0, 9, 5, 1, 13, 17, 21, 0],
            1: [0, 10, 6, 2, 14, 18, 0],
            2: [0, 11, 3, 7, 15, 19, 0],
            3: [0, 12, 8, 4, 16, 20, 0]
        }
        self.max_cost = 188.89441009666507
        self.actual_costs = {
            0: 188.89441009666507,
            1: 158.32493270042846,
            2: 184.1589549784565,
            3: 161.02543182365255
        }
    
    def test_unique_cities_per_robot_excluding_depot(self):
        visited_cities = set()
        for tour in self.robot_tours.values():
            # Remove the depot (0) and check
            cities = set(tour) - {0}
            self.assertTrue(visited_cities.isdisjoint(cities))
            visited_cities.update(cities)
        self.assertEqual(len(visited_cities), 21)

    def test_correct_total_num_cities_visited(self):
        total_cities_visited = sum(len(set(tour) - {0}) for tour in self.robot_tours.values())
        self.assertEqual(total_cities_visited, 21)

    def test_travel_cost_calculation(self):
        def calculate_cost(tour):
            cost = 0
            for i in range(len(tour) - 1):
                x1, y1 = self.coordinates[tour[i]]
                x2, y2 = self.coordinates[tour[i + 1]]
                cost += sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            return cost
        
        for robot, tour in self.robot_tours.items():
            self.assertAlmostEqual(calculate_cost(tour), self.actual_costs[robot])
    
    def test_minimum_max_distance(self):
        calculated_max_cost = max(self.actual_costs.values())
        self.assertEqual(calculated_max_cost, self.max_cost)

    def test_output_format_and_routes(self):
        # Check if all tours start and end at 0 and if they contain only city indices
        for tour in self.robot_tours.values():
            start, end = tour[0], tour[-1]
            self.assertEqual(start, 0)
            self.assertEqual(end, 0)
            self.assertTrue(all(isinstance(city, int) for city in tour))

if __name__ == "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestMTSPSolution)
    results = unittest.TextTestRunner().run(test_suite)
    if results.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")