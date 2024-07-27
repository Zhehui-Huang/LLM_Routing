import unittest
import math

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        # Setup environment and robot information
        self.cities = {
            0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
            4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
            8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
            12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
            16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
            20: (155, 185), 21: (139, 182)
        }
        self.robot_tours = {
            0: [0, 1, 8, 10],
            1: [0, 19, 20, 21, 17, 13],
            2: [0, 11, 4, 3, 16, 15, 5, 18, 12, 14, 6, 2],
            3: [0, 9, 7]
        }
        self.reported_costs = {
            0: 102.41886165888774,
            1: 130.4047119394745,
            2: 357.2113605170252,
            3: 65.36789834516586
        }
        self.expected_total_cost = 655.4028324605532

    def test_unique_city_visit(self):
        all_visited = []
        for tour in self.robot_tours.values():
            all_visited.extend(tour)
        unique_cities = set(all_visited)
        # Check all cities are visited once
        self.assertEqual(len(unique_cities), len(self.cities))

    def test_all_cities_visited(self):
        all_cities_set = set(self.cities.keys())
        visited_cities_set = set()
        for tour in self.robot_tours.values():
            visited_cities_set.update(set(tour[1:-1])) # excluding the repeated depot city at start and end
        self.assertEqual(all_cities_set, visited_cities_set)

    def test_total_costs(self):
        calculated_total_cost = 0
        # Calculate costs for each tour and check with reported
        for robot_id, tour in self.robot_tours.items():
            cost = 0
            for i in range(len(tour) - 1):
                cost += calculate_distance(self.cities[tour[i]], self.cities[tour[i+1]])
            calculated_total_cost += cost
            self.assertAlmostEqual(cost, self.reported_costs[robot_id], places=5)
        
        # Check the overall cost
        self.assertAlmostEqual(calculated_total_cost, self.expected_total_cost, places=5)

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTours)
    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

# Run tests and provide output
test_result = run_tests()
print(test_result)