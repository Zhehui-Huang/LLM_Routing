import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_travel_cost, city_coordinates, city_groups):
    # Verify tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Extract visited cities from the tour (excluding the initial and final depot city)
    visited_citites = set(tour[1:-1])
    
    # Check if exactly one city from each group is visited
    if not all(any(city in group for city in visited_citites) for group in city_groups):
        return "FAIL"
    
    # Verify each group has exactly one city in the tour
    count = 0
    for group in city_groups:
        if sum(city in visited_citites for city in group) != 1:
            return "FAIL"
        count += 1

    # Verify traveled path cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculateborne_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Define city coordinates and city groups
city_coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]
city_groups = [
    [1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]
]

# Tour and total cost provided
tour = [0, 12, 11, 8, 10, 9, 14, 0]
total_travel_cost = 214.92

# Perform the verification
result = verify_solution(tour, total_travel_result, city_coordinates, city_groups)
print(result)