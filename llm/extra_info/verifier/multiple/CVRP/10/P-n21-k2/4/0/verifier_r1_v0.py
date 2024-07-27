import math
import unittest

# City coordinates and demand list
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Robots info
robot_tours = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    [0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0]
]
robot_costs = [187.81, 287.43]
robot_capacities = [160, 160]


def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class TestVRPSolution(unittest.TestCase):

    def test_city_count(self):
        """There should be 21 cities including the depot."""
        self.assertEqual(len(cities), 21)

    def test_demand_met(self):
        """Each city demand must be met exactly."""
        demand_met = [0] * len(cities)
        for tour in robot_tours:
            for i in range(1, len(tour) - 1):
                demand_met[tour[i]] += demands[tour[i]]
        self.assertListEqual(demand_met, demands)

    def test_robot_capacities(self):
        """Each robot must not exceed its carrying capacity."""
        for tour_index, tour in enumerate(robot_tours):
            load = sum(demands[city] for city in tour[1:-1])
            self.assertLessEqual(load, robot_capacities[tour_index])

    def test_tours_begin_end_depot(self):
        """Each tour must start and end at the depot (City 0)."""
        for tour in robot_tours:
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

    def test_cost_calculation(self):
        """Costs must be calculated as Euclidean distance and summed correctly."""
        for tour_index, tour in enumerate(robot_tours):
            cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
            self.assertAlmostEqual(cost, robot_costs[tour_index], places=2)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVRPSolution)
    test_result = unittest.TextTestRunner().run(suite)
    if test_result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

# Running the tests to verify the solution
main()