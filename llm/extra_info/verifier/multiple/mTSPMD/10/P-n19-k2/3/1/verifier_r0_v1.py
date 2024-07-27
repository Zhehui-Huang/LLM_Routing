import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def verify_solution(cities, robot_tours):
    # Ensure all cities are visited exactly once and the tour starts/ends at the assigned depots
    visited_cities = set()
    depot_starts = [tour[0] for tour in robot_tours]
    depot_ends = [tour[-1] for tour in robot_tours]

    for tour in robot_tours:
        if tour[0] != tour[-1]:
            return "FAIL"
        visited_cities.update(tour)

    if visited_cities != set(range(len(cities))) or sorted(depot_starts) != sorted(depot_ends):
        return "FAIL"

    # Compute and validate travel costs
    robot_actual_costs = []
    expected_costs = [112.0719227360316, 151.74982440173858]
    for tour, expected_cost in zip(robot_tours, expected_costs):
        actual_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
        robot_actual_costs.append(actual_cost)
        if not math.isclose(actual_cost, expected_cost, rel_tol=1e-9):
            return "FAIL"

    # Check the total cost
    total_actual_cost = sum(robot_actual_costs)
    expected_total_cost = sum(expected_costs)
    if not math.isclose(total_actual—

import itertools
unittest import TestCase

class TestRouteSolution(TestCase):
    def test_routes(self):
        cities = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
                  (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]

        robot_tours = [
            [0, 6, 2, 7, 5, 9, 8, 3, 4, 0],  # Robot 0 Tour
            [1, 10, 12, 14, 11, 16, 17, 15, 13, 18, 1]  # Robot 1 Tour
        ]

        result = verify_solution(cities, robot_tours)
        self.assertEqual(result, "CORRECT", "The verification of the routes should be CORRECT")

# Running the test
if __name__ == "__main__":
    unittest.main()