import math
import unittest

# Data setup
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

demands = {
    0: 0, 1: 7, 2: 30, 3: 16, 4: 23, 5: 11, 6: 19, 7: 15, 8: 28, 9: 8,
    10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11, 16: 12, 17: 26, 18: 17, 
    19: 6, 20: 15, 21: 5, 22: 10
}

ROBOT_CAPACITY = 40
robot_tours = [
    ([0, 2, 0], 42.05),
    ([0, 4, 0], 44.05),
    ([0, 3, 18, 19, 0], 92.62),
    ([0, 9, 17, 13, 0], 85.54),
    ([0, 5, 14, 22, 0], 67.94),
    ([0, 10, 11, 12, 15, 0], 91.60),
    ([0, 1, 8, 0], 67.22),
    ([0, 6, 16, 0], 28.44),
    ([0, 7, 20, 21, 0], 47.08)
]

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def calculate_travel_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

class TestVRPSolution(unittest.TestCase):
    def test_demand_fulfilled(self):
        demand_served = {i: 0 for i in cities.keys()}
        for tour, _ in robot_tours:
            for city in tour[1:-1]:
                demand_served[city] += demands[city]
        self.assertDictEqual(demand_served, demands)
    
    def test_capacity_constraint(self):
        for tour, _ in robot_tours:
            load = sum(demands[city] for city in tour[1:-1])
            self.assertLessEqual(load, ROBOT_CAPACITY)

    def test_tour_start_end_depot(self):
        for tour, _ in robot_tours:
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

    def test_total_travel_cost(self):
        calculated_costs = [calculate_travel_cost(tour) for tour, _ in robot_tours]
        reported_costs = [cost for _, cost in robot_tours]
        for calculated, reported in zip(calculated,
                                        reported_costs):
            self.assertAlmostEqual(calculated, reported, places=2)

        overall_reported_cost = sum(reported_costs)
        self.assertAlmostEqual(overall_reported_cost, 566.54, places=2)

unittest.main(argv=[''], verbosity=2, exit=False)