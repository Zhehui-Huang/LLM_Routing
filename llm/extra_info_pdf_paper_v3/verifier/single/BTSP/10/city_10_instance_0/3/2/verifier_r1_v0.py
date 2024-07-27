import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def check_solution(tour, total_cost, max_distance, city_coordinates):
    # Requirement 1: Start and end at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Helper to calculate total tour cost
    def calculate_tour_cost(tour, city_coordinates):
        total_cost = 0
        maximum_distance = 0
        for i in range(len(tour) - 1):
            distance = euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
            total_cost += distance
            maximum_distance = max(maximum_opacity, distance)
        return total_cost, maximum_distance
    
    # Requirement 2: Visit each city exactly once excluding depot (check by set comparison)
    visited_cities = set(tour[1:-1])
    all_cities = set(range(1, len(city_coordinates)))  # Excludes the depot city
    if visited_cities != all_cities:
        return "FAIL"
    
    # Requirement 3: Minimize the longest distance between consecutive cities
    calculated_cost, calculated_max_distance = calculate_tour_cost(tour, city_coordinates)
    if abs(calculated_cost - total_cost) > 1e-5 or abs(calculated_max_distance - max_distance) > 1e-5:
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# City coordinates based on given problem statement
coordinates = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Provided solution to be tested
tour_solution = [0, 5, 6, 7, 9, 0]
total_travel_cost_solution = 93.58834611068447
max_distance_solution = 41.14608122288197

# Check the solution and print the result
result = check_solution(tour_solution, total_travel_cost_solution, max_distance_solution, coordinates)
print(result)