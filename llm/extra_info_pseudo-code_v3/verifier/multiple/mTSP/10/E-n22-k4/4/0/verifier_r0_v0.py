import unittest
import math

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        # City coordinates with city index as key
        self.cities = {
            0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
            5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
            10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
            15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
            20: (155, 185), 21: (139, 182)
        }
        
        # Tours from solution
        self.robot_tours = {
            0: [0, 13, 17, 21, 9, 5, 1, 0],
            1: [0, 14, 18, 10, 6, 2, 0],
            2: [0, 15, 7, 3, 11, 19, 0],
            3: [0, 16, 12, 8, 4, 20, 0]
        }
        
        # Expected total travel costs of individual robot tours
        self.expected_costs = {
            0: 197.5591024687469,
            1: 154.7311246419968,
            2: 183.24946422163586,
            3: 177.4902176700044
        }

    def test_city_visit_once(self):
        visited = set()
        for tour in self.robot_tours.values():
            # Check excluding start and end city (the depot)
            self.assertTrue(tour[0] == 0 and tour[-1] == 0)
            for city in tour[1:-1]:
                # Ensure each city is visited only once
                self.assertNotIn(city, visited)
                visited.add(city)

        # Check if all cities except depot were visited
        self.assertEqual(visited, set(self.cities.keys()) - {0})

    def test_travel_cost(self):
        for robot_id, tour in self.robot_tours.items():
            calculated_cost = 0
            for i in range(len(tour) - 1):
                city1 = self.cities[tour[i]]
                city2 = self.cities[tour[i + 1]]
                calculated_cost += math.hypot(city2[0] - city1[0], city2[1] - city1[1])
            # Check if the calculated cost is close to the expected cost
            self.assertAlmostEqual(calculated_cost, self.expected_costs[robotid], places=5)

    def test_output(self):
        total_cost = sum(self.expected_costs.values())
        self.assertAlmostEqual(total_cost, 713.029909002384, places=5)

    def test_num_robots_used(self):
        self.assertEqual(len(self.robot_tours), 4)

if __name__ == "__main__":
    unittest.main()