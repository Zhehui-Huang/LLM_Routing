import math
import unittest

# Cities coordinates based on the problem statement
cities = [
    (16, 90),  # Depot city 0
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# Expected results based on the provided solution
tour = [0, 14, 5, 9, 13, 10, 8, 6, 1, 4, 12, 3, 7, 11, 2, 0]
total_travel_cost_provided = 373.61498801130097
max_distance_provided = 94.11163583744573

def calculate_euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_tour(tour, cities):
    visited = set(tour)
    total_cost = 0
    max_distance = 0
    
    if tour[0] != tour[-1] or tour[0] != 0:
        return "FAIL"

    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        dist = calculate_euclidean_distance(cities[city1], cities[city2])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
            
    if total_cost != total_travel_cost_provided:
        return "FAIL"
    if max_distance != max_distance_provided:
        return "FAIL"
    if len(visited) != len(cities):
        return "FAIL"
    
    return "CORRECT"

# Unit test class to verify the solution's validity
class TestTSPSolution(unittest.TestCase):
    def test_solution_validity(self):
        result = validate_tour(tour, cities)
        self.assertEqual(result, "CORRECT", "The provided tour fails to meet the requirements")

# Execute the tests
if __name__ == "__main__":
    unittest.main()