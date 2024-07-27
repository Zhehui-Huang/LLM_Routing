import unittest
from math import sqrt

# Data for cities: index and coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Provided tour
tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
total_travel_cost = 458.36719998557066
max_distance_between_cities = 68.15423684555495

def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_tour(tour, cities):
    # Check if the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once
    visited = set(tour)
    if len(visited) != len(cities) + 1 or any(tour.count(city) != 1 for city in range(1, len(cities))):
        return "FAIL"
    
    # Check total cost and maximum distance
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        total_cost += distance
        max_distance = max(max_distance, distance)
    
    if not (abs(total_cost - total_travel_cost) < 0.001 and abs(max_distance - max_distance_between_cities) < 0.001):
       return "FAIL"
    
    return "CORRECT"

class TestTourSolution(unittest.TestCase):
    def test_solution(self):
        result = check_tour(tour, cities)
        self.assertEqual(result, "CORRECT")

unittest.main(argv=[''], verbosity=2, exit=False)