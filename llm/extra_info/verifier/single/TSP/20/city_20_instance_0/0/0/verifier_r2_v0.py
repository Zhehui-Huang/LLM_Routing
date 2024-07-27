import math
from typing import List, Tuple

# Given coordinates for each city
city_coordinates = [
    (8, 11),    # Depot city 0
    (40, 6),    # City 1
    (95, 33),   # City 2
    (80, 60),   # City 3
    (25, 18),   # City 4
    (67, 23),   # City 5
    (97, 32),   # City 6
    (25, 71),   # City 7
    (61, 16),   # City 8
    (27, 91),   # City 9
    (91, 46),   # City 10
    (40, 87),   # City 11
    (20, 97),   # City 12
    (61, 25),   # City 13
    (5, 59),    # City 14
    (62, 88),   # City 15
    (13, 43),   # City 16
    (61, 28),   # City 17
    (60, 63),   # City 18
    (93, 15)    # City 19
]

# Tour and total travel cost provided in the solution
proposed_tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
proposed_total_cost = 349.1974047195548

def calculate_euclidean_distance(city1: Tuple[int, int], city2: Tuple[int, int]) -> float:
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour_requirements(tour: List[int], total_cost: float) -> str:
    # [Requirement 1] and [Requirement 4]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2]
    unique_cities = set(tour)
    if len(unique_cities) != 21 or len(tour) != 21:  # Includes all cities plus the starting/ending depot
        return "FAIL"
    
    # Calculate total travel cost and compare with the given cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_index_1 = tour[i]
        city_index_2 = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(city_coordinates[city_index_1], city_coordinates[city_index_2])
    
    # [Requirement 3] and [Requirement 5]
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Evaluate if the provided solution is correct based on requirements
result = verify_tour_requirements(proposed_tour, proposed_total_cost)
print(result)