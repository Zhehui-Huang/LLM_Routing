import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tsp_solution(tour, total_travel_cost, maximum_distance):
    cities_coordinates = [
        (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
        (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), 
        (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
    ]
    
    # Requirement 1: Check start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Check each city visited exactly once
    if sorted(tour) != sorted(list(set(tour))):
        return "FAIL"
    if len(tour) != len(set(tour)):
        return "FAIL"
    
    # Calculate actual total travel cost and max distance between consecutive cities
    actual_total_cost = 0
    actual_max_distance = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        distance = calculate_euclidean_distance(*cities_coordinates[city1], *cities_coordinates[city2])
        actual_total_cost += distance
        actual_max_distance = max(actual_max_distance, distance)

    # Requirement 3: Check total cost and maximum distance
    if not (math.isclose(actual_total_cost, total_travel_cost, rel_tol=1e-2) and
            math.isclose(actual_max_distance, maximum_distance, rel_tol=1e-2)):
        return "FAIL"

    return "CORRECT"

# Given solution details
tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
total_travel_cost = 458.37
maximum_distance = 68.15

# Verify the solution
result = verify_tsp_solution(tour, total_travel_cost, maximum_distance)
print(result)