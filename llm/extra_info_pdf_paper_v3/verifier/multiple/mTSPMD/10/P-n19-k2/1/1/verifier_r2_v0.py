import unittest
import math

# City coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
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
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def calculate_total_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

class TestTSPSolution(unittest.TestCase):
    def test_solution_correctness(self):
        robot_0_tour = [0, 6, 6, 0]
        robot_1_tour = [1, 6, 6, 1]

        # Checking Requirement 3 and 6: All cities should be visited exactly once, excluding depots
        all_cities_visited = set(robot_0_tour[1:-1] + robot_1_tour[1:-1]) == set(range(2, 19))

        # Checking robots' tours start and end at their depot
        correct_depot_start_end = (robot_0_tour[0] == robot_0_tour[-1] == 0) and (robot_1_tour[0] == robot_1_tour[-1] == 1)

        # Calculate travel costs
        robot_0_cost = calculate_total_tour_cost(robot_0_tour)
        robot_1_cost = calculate_total_tour_cost(robot_1_tour)
        total_cost = robot_0_cost + robot_1_cost

        # Checking Requirement 4: total travel cost
        min_cost = total_cost < 48.249281104773736

        # Checking if each city was visited exactly once and each robot returned to start
        self.assertTrue(all_cities_visited and correct_depot_start_end and min_cost, "FAIL")
        
        print("CORRECT")

# Run the tests
unittest.main(argv=[''], verbosity=2, exit=False)