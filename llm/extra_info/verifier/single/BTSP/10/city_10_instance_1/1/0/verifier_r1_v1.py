import math
from typing import List, Tuple

def calculate_distance(city1: Tuple[int, int], city2: Tuple[int, int]) -> float:
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(cities: List[Tuple[int, int]], tour: List[int], reported_total_cost: float, reported_max_distance: float) -> str:
    # Check Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: Every city visited once
    if sorted(tour) != sorted(list(range(len(cities)))):
        return "FAIL"
    
    # Calculate actual travel cost and max distance
    total_cost = 0
    max_distance = 0
    for idx in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[idx]], cities[tour[idx + 1]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    
    # Round calculations to two decimals
    total_cost = round(total_cost, 2)
    max_distance = round(max_distance, 2)
    
    # Check calculations against reported values
    if abs(total_cost - reported_total_cost) > 0.01 or abs(max_distance - reported_max_distance) > 0.01:
        return "FAIL"

    return "CORRECT"

# Given city coordinates
cities_coordinates = [
    (53, 68),  # City 0 - Depot
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

# Provided solution
tour_solution = [0, 4, 8, 3, 5, 2, 9, 7, 1, 6, 0]
total_travel_cost = 278.93
max_distance_consecutive_cities = 56.61

# Verify the solution
result = verify_solution(cities_coordinates, tour_solution, total_travel_cost, max_distance_consecutive_cities)
print(result)