import unittest
import math

# Define the cities coordinates
cities = [
    (9, 93),  # City 0 - Depot
    (8, 51),  # City 1
    (74, 99), # City 2
    (78, 50), # City 3
    (21, 23), # City 4
    (88, 59), # City 5
    (79, 77), # City 6
    (63, 23), # City 7
    (19, 76), # City 8
    (21, 38), # City 9
    (19, 65), # City 10
    (11, 40), # City 11
    (3, 21),  # City 12
    (60, 55), # City 13
    (4, 39)   # City 14
]

# Expected outputs
expected_tour = [0, 8, 10, 1, 11, 14, 9, 4, 12, 7, 3, 5, 6, 2, 13, 0]
expected_total_cost = 373.97
expected_max_distance = 63.6

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def validate_tour(tour, cities):
    visited = set(tour)
    total_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    max_distance = max(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    return (
        tour[0] == tour[-1] == 0,  # Starts and ends at depot
        visited == set(range(len(cities))),  # Visits all cities
        len(visited) == len(tour) - 1,  # Visit each city exactly once
        abs(total_cost - expected_total_check) < 0.01,  # Tolerance for floating point arithmetic
        abs(max_distance - expected_max_distance_check) < 0.01  # Tolerance for floating point arithmetic
    )

class TestVRPSolution(unittest.TestCase):
    def test_validate_solution(self):
        is_correct_start_end, includes_all_cities, visit_once, correct_total_cost, correct_max_distance = validate_tour(expected_tour, cities)
        self.assertTrue(is_correct_start_end)
        self.assertTrue(includes_all_cities)
        self.assertTrue(visit_once)
        self.assertTrue(correct_total_cost)
        self.assertTrue(correct_max_distance)

# Run the tests
if __name__ == '__main__':
    unittest.main()