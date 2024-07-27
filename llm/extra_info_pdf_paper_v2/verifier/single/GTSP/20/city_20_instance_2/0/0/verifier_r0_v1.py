import unittest
import math

# Coordinates of cities, including the depot as city 0
city_coordinates = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Groups
city_groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

def calculate_euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_travel_cost(tour):
    """ Calculate the total travel cost for a given tour """
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(tour[i], tour[i + 1])
    return total_cost

class TestRobotTour(unittest.TestCase):
    def test_tour_correctness(self):
        proposed_solution = [0, 7, 3, 1, 5, 2, 0]
        proposed_cost = 279.21

        # Check if starts and ends at depot
        self.assertEqual(proposed_solution[0], 0)
        self.assertEqual(proposed_solution[-1], 0)
        
        # Check if each group is represented exactly once in the tour
        visited_groups = []
        for city in proposed_solution[1:-1]:  # Excluding the depot at start and end
            for index, group in enumerate(city_groups):
                if city in group:
                    visited_groups.append(index)
        self.assertTrue(len(set(visited_groups)) == len(city_groups))
        
        # Check if calculated tour cost is correct
        calculated_cost = total_travel_cost(proposed_space)
        self.assertAlmostEqual(calculated_cost, proposed_cost, places=2)

        if len(set(visited_groups)) == len(city_groups) and abs(calculated_cost - proposed_cost) < 1e-2:
            print("CORRECT")
        else:
        	print("FAIL")

unittest.main(argv=[''], verbosity=2, exit=False)