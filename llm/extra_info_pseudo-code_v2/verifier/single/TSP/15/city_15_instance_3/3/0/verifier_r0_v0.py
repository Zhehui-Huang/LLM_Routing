import unittest
from math import sqrt

def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_tour_requirements(tour, cities, reported_cost):
    # Check start and end at depot city (Requirement 1)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once (Requirement 2)
    visited = sorted(tour[1:-1])
    if visited != list(range(1, len(cities))):
        return "FAIL"
    
    # Calculating total tour distance (Requirement 3)
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Check if reported and calculated distances match (Requirement 4)
    if not (abs(total_distance - reported_cost) < 1E-2):  # Allowing a small error margin
        return "FAIL"
    
    return "CORRECT"

class TestTSPSolution(unittest.TestCase):
    def test_tsp(self):
        cities = [
            (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
            (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
            (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
        ]
        tour = [0, 14, 5, 9, 13, 10, 8, 6, 1, 4, 12, 3, 7, 11, 2, 0]
        reported_cost = 373.61
        result = check_tour_requirements(tour, cities, reported_cost)
        self.assertEqual(result, "CORRECT")

if __name__ == "__main__":
    unittest.main()