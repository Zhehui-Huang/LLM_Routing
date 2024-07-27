import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
            5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
            10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
            15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
        }

        self.robot_tours = [
            [0, 2, 5, 13, 15, 9, 7, 6, 18, 0],
            [1, 4, 10, 12, 3, 8, 16, 17, 14, 11, 1]
        ]

        # Calculate initial travel costs
        self.tour_costs = [0, 0]
        self.total_cost = 0
        for robot_id, tour in enumerate(self.robot_tours):
            for i in range(len(tour) - 1):
                self.tour_costs[robot_id] += calculate_distance(self.cities[tour[i]], self.cities[tour[i + 1]])
            self.total_cost += self.tour_costs[robot_id]

    def test_each_robot_starts_and_ends_at_depot(self):
        for robot_id, tour in enumerate(self.robot_tours):
            depot = tour[0]
            self.assertEqual(depot, tour[-1])

    def test_all_cities_visited_exactly_once(self):
        visited_cities = set()
        for tour in self.robot_tours:
            visited_cities.update(tour[:-1])  # excluding the last city since it's the depot and repeated.
        self.assertEqual(len(visited_cities), 19)

    def test_correct_output_format(self):
        self.assertIsInstance(self.robot_tours, list)
        self.assertIsInstance(self.total_cost, (int, float))
        for cost in self.tour_costs:
            self.assertIsInstance(cost, (int, float))

    def test_costs_are_calculated_correctly(self):
        recalculated_costs = []
        for tour in self.robot_tours:
            tour_cost = sum(calculate_distance(self.cities[tour[i]], self.cities[tour[i+1]]) for i in range(len(tour)-1))
            recalculated_costs.append(tour_cost)
        
        for calculated, expected in zip(recalculated_costs, self.tour_costs):
            self.assertAlmostEqual(calculated, expected, places=2)
        
        recalculated_total = sum(recalculated_costs)
        self.assertAlmostEqual(recalculated_total, self.total_cost, places=2)

# Run tests (if script is executable)
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)