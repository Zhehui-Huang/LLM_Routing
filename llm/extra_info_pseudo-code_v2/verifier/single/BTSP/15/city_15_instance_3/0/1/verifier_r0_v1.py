import math
import unittest

# Given city coordinates
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

# Input solution
tour = [0, 14, 5, 9, 13, 10, 8, 6, 1, 4, 12, 3, 7, 11, 2, 0]
total_travel_cost_provided = 373.61498801130097
max_distance_provided = 94.11163583744573

def calculate_euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def evaluate_tour(tour, max_allowed_distance):
    visited = set(tour)
    total_cost = 0
    max_distance = 0

    for i in range(len(tour) - 1):
        dist = calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist

    requirement_1 = len(visited) == len(cities) and len(tour) - 1 == len(cities)
    requirement_2 = tour[0] == tour[-1] == 0
    requirement_3 = max_distance == max_allowed_distance

    return requirement_1, requirement_2, requirement_3, total_cost, max_distance

class TestTSPSolution(unittest.TestCase):
    def test_solution_validity(self):
        req1, req2, req3, calculated_cost, calculated_max_dist = evaluate_tour(tour, max_distance_provided)
        self.assertTrue(req1, "Each city is not visited exactly once")
        self.assertTrue(req2, "Tour does not start and end at the depot")
        self.assertTrue(req3, "Max distance between consecutive cities does not match provided")
        self.assertAlmostEqual(calculated_cost, total_travel_cost_provided, places=2, msg="Total travel cost does not match")

if __name__ == "__main__":
    unittest.main()