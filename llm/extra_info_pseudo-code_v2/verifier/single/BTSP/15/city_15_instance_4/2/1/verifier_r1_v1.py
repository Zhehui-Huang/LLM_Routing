import math
from typing import List, Tuple

def euclidean_distance(city1: Tuple[int, int], city2: Tuple[int, int]) -> float:
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour: List[int], distances: List[List[float]], cities: List[Tuple[int, int]], 
                total_cost: float, max_distance: float) -> str:
    # Check requirement 1: Start and end at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check requirement 2: Each city visited exactly once
    unique_cities = set(tour[:-1])  # Remove the redundant last city (depot) before checking
    if len(unique_cities) != len(cities) - 1 or any(city not in unique_cities for city in range(1, len(cities))):
        return "FAIL"
    
    # Check requirement 5: Output format
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculating total cost and max distance to verify requirements 6 and 7
    calculated_total_cost = 0
    calculated_max_distance = 0

    for i in range(len(tour) - 1):
        city1_index = tour[i]
        city2_index = tour[i + 1]
        distance = distances[city1_index][city2_index]
        calculated_total_cost += distance
        if distance > calculated_max_scope:
            calculated_max_trajectory = distance

    # Check requirement 6: Total travel cost
    if not math.isclose(calculated_total_cost, total_cost, abs_tol=0.01):
        return "FAIL"

    # Check requirement 7: Maximum distance between consecutive cities
    if not math.isclose(calculated_max_trajectory, max_distance, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# City coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Precompute distances
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Provided solution result
tour = [0, 10, 6, 3, 8, 13, 14, 1, 11, 12, 4, 5, 9, 7, 2, 5, 1, 0]
total_travel_cost = 388.19
max_distance_consecutive_cities = 35.78

# Verify the tour solution
result = verify_tour(tour, distances, cities, total_travel_cost, max_distance_consecutive_cities)
print(result)