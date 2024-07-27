import unittest
import math

# Coordinates for each city, indexed by the city's identifier.
cities = {
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
    20: (45, 35)
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

class TestTSPSolution(unittest.TestCase):
    def test_solution(self):
        # Provided tours and their costs
        tours = {
            0: [0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 0],
            1: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 0]
        }
        reported_costs = {
            0: 315.59626267046633,
            1: 262.9738751557865
        }
        reported_total_cost = 578.5701378262529

        # Check for total and individual costs calculation
        calculated_costs = {robot: calculate_tour_cost(tour) for robot, tour in tours.items()}
        calculated_total_cost = sum(calculated_costs.values())

        # Validate costs
        for robot, cost in reported_costs.items():
            self.assertAlmostEqual(calculated_costs[robot], cost, places=5)

        self.assertAlmostEqual(calculated_total_cost, reported_total_cost, places=5)

        # Validate all cities are visited exactly once
        all_visited = set()
        for tour in tours.values():
            all_visited.update(tour[1:-1])  # exclude the starting and ending depot

        self.assertEqual(len(all_visited), 20)
        self.assertEqual(all_visited, set(range(1, 21)))  # Cities from 1 to 20

        # Confirm tours start and end at depot
        for tour in tours.values():
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

if __name__ == "__main__":
    unittest.main(argv=['ignored', '-v'], exit=False)  # Updated to handle Jupyter Notebook environment