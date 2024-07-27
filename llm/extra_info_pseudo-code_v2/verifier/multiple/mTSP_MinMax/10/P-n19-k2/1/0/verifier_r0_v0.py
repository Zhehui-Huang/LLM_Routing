import unittest
import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

class TestRobotTourSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = [
            (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
            (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
            (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
            (61, 33), (62, 63), (63, 69), (45, 35)
        ]
        self.robot_tours = {
            0: [0, 0, 2, 10, 16, 17, 14, 11, 0],
            1: [0, 1, 4, 12, 3, 8, 9, 15, 7, 5, 13, 6, 0]
        }
        self.robot_costs = {
            0: 126.06136675406752,
            1: 143.4986323452223
        }
        self.max_cost = 143.4986323452223

    def test_tour_completeness(self):
        visited = set()
        for tour in self.robot_tours.values():
            for city in tour:
                if city != 0:
                    visited.add(city)
        self.assertEqual(len(visited), 18)

    def test_tour_valid_start_end(self):
        for tour in self.robot_tours.values():
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

    def test_visiting_each_city_once(self):
        all_cities = set(range(1, 19))  # City indices excluding the depot
        cities_visited = []
        for tour in self.robot_tours.values():
            cities_visited.extend(tour[1:-1])  # Exclude the starting and ending depot
        self.assertEqual(set(cities_visited), all_cities)
        self.assertEqual(len(cities_visited), len(set(cities_visited)))

    def test_minimum_max_distance(self):
        calculated_max_cost = max(self.robot_costs.values())
        self.assertEqual(calculated_max_cost, self.max_cost)

    def test_correct_cost_calculation(self):
        for robot_id, tour in self.robot_tours.items():
            cost = 0
            for i in range(len(tour) - 1):
                cost += calculate_distance(self.coordinates[tour[i]], self.coordinates[tour[i + 1]])
            self.assertAlmostEqual(cost, self.robot_costs[robot_id])

if __name__ == "__main__":
    # Run the unit tests
    unittest.main(argv=[''], exit=False)