import math
import unittest

# City Coordinates, indexed by city number
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
    """Calculate the Euclidean distance between two cities"""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def tour_cost(tour):
    """Calculate the total cost of a given tour"""
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

class TestTSPSolution(unittest.TestCase):
    def test_solution(self):
        # Given tours and their reported costs
        tours = {
            0: [0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 0],
            1: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 0]
        }
        reported_costs = {
            0: 315.59626267046633,
            1: 262.9738751557865
        }
        reported_total_cost = 578.5701378262529

        # Calculating total costs from the tours
        calculated_costs = {robot: tour_cost(tour) for robot, tour in tours.items()}
        calculated_total_cost = sum(calculated_costs.values())

        # Checking individual and total travel costs
        for robot in tours:
            self.assertAlmostEqual(calculated_costs[robot], reported_costs[robot], places=5)

        # Check the overall total cost
        self.assertAlmostEqual(calculated_total_cost, reported_total_cost, places=5)

        # Setup visiting verification
        all_visited = set()
        for tour in tours.values():
            for city in tour[1:-1]: # exclude the depot from the set
                all_visited.add(city)

        # All cities visited exactly once
        self.assertEqual(len(all_all_visited), 20) # because depot is not counted in visits
        self.assertEqual(set(all_all_visited), set(range(1, 21)))

        # Tours properly start and end at the Depot
        for tour in tours.values():
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

# Run the test
if __name__ == "__main__":
    unittest.main()