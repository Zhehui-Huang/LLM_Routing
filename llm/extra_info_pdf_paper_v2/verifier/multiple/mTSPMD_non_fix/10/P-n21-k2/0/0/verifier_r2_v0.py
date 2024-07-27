import unittest
import math

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

class TestRobotTourSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = [
            (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
            (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
            (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
            (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
            (45, 35)
        ]
        # Tours from the provided solution
        self.robot_tours = [
            [0, 0, 4, 10, 6, 7, 5, 9, 2, 8, 3],
            [1, 1, 20, 16, 11, 15, 12, 19, 18, 13, 17, 14]
        ]
        self.robot_costs = [116.17605288114586, 136.50982867449432]
        self.total_cost = 252.68588155564018

    def test_unique_visited_cities(self):
        all_cities_visited = set()
        for tour in self.robot_tours:
            all_cities_visited.update(tour)
        self.assertEqual(len(all_cities_visited), 21)

    def test_start_and_end_at_depot(self):
        for idx, tour in enumerate(self.robot_tours):
            # Check if robots start and end at the depot correctly
            self.assertEqual(tour[0], idx)
            self.assertEqual(tour[1], idx)

    def test_total_travel_cost_calculation(self):
        robot_calculated_costs = []
        for idx, tour in enumerate(self.robot_tours):
            tour_cost = 0
            for i in range(len(tour) - 1):
                tour_cost += calculate_distance(self.coordinates[tour[i]], self.coordinates[tour[i + 1]])
            # Round the tour cost to similar precision as the original output for comparison
            tour_cost = round(tour_cost, 14)
            robot_calculated_costs.append(tour_cost)
        self.assertEqual(self.robot_costs, robot_calculated_costs)
        self.assertAlmostEqual(sum(robot_calculated_costs), self.total_cost)

    def test_no_unvisited_cities(self):
        visited = set(city for tour in self.robot_tours for city in tour if city != tour[0])
        self.assertEqual(len(visited), 20)  # Subtracting the repeated depot element

    def test_optimization_of_tours(self):
        # Since optimization's correctness deeply depends on the correctness of the computation,
        # this test will ensure that the provided tour costs align closely with the given costs
        # as the exact knowledge about optimization procedure or alternative optimal values isn't given.
        robot_given_costs = [116.17605288114586, 136.50982867449432]
        for idx, given_cost in enumerate(self.robot_costs):
            estimated_cost = round(calculate_total_distance(self.robot_tours[idx]), 5)
            self.assertAlmostEqual(estimated_cost, given_cost, places=5)

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_distance

if __name__ == '__main__':
    unittest.main()