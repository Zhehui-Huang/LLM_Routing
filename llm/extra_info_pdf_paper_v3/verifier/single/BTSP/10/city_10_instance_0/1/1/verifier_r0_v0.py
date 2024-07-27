import math
from typing import List, Tuple

def euclidean_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_total_travel_cost(route: List[int], locations: List[Tuple[int, int]]) -> float:
    total_cost = 0.0
    for i in range(len(route) - 1):
        total_cost += euclidean_distance(locations[route[i]], locations[route[i + 1]])
    return total_cost

def calculate_maximum_distance(route: List[int], locations: List[Tuple[int, int]]) -> float:
    max_dist = 0.0
    for i in range(len(route) - 1):
        dist = euclidean_distance(locations[route[i]], locations[route[i + 1]])
        if dist > max_dist:
            max_dist = dist
    return max_dist

def test_solution(route: List[int], total_cost: float, max_dist: float):
    locations = [
        (50, 42), # city 0
        (41, 1),  # city 1
        (18, 46), # city 2
        (40, 98), # city 3
        (51, 69), # city 4
        (47, 39), # city 5
        (62, 26), # city 6
        (79, 31), # city 7
        (61, 90), # city 8
        (42, 49)  # city 9
    ]
    
    # Check for route starting and ending at city 0
    if route[0] != 0 or route[-1] != 0:
        return "FAIL"
    
    # Check if robot visits each city exactly once
    unique_cities = set(route)
    if len(unique_cities) != 10 or len(route) != 11:  # including depot city twice
        return "FAIL"
    
    # Calculate and compare total travel cost
    calculated_total_cost = calculate_total_travel_cost(route, locations)
    if not math.isclose(calculated_total_cost, total_cost, abs_tol=0.01):
        return "FAIL"

    # Calculate and compare maximum distance between consecutive cities
    calculated_max_distance = calculate_maximum_distance(route, locations)
    if not math.isclose(calculated_max_distance, max_dist, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Test data from the solution
route = [0, 1, 5, 2, 4, 3, 8, 9, 6, 7, 0]
total_travel_cost = 328.3966856465968
maximum_distance = 45.18849411078001

# Validate the provided solution
result = test_solution(route, total_travel_cost, maximum_distance)
print(result)