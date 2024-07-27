import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_solution(tour, total_cost):
    # City coordinates - indexed from 0 to 19
    coordinates = [
        (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), 
        (45, 84), (4, 56), (54, 82), (37, 28), (27, 45), 
        (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), 
        (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
    ]
    
    # Check Requirement 1: Tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: Each city must be visited exactly once
    unique_cities = set(tour[1:-1])  # Excluding the first and last which are depot city
    if len(unique_cities) != 19 or set(range(1, 20)) != unique_cities:
        return "FAIL"
    
    # Check Requirement 3 and Requirement 4: Calculate total travel cost and verify it
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    
    if abs(calculated_cost - total_cost) > 1e-6:
        return "FAIL"
    
    # Check Requirement 5: Ensure no subtours
    visited = [False] * 20
    for i in range(len(tour) - 1):
        if visited[tour[i]]:
            return "FAIL"
        visited[tour[i]] = True

    return "CORRECT"

# Given tour and cost
tour = [0, 14, 3, 0, 14, 3, 0, 14, 3, 0, 14, 3, 0, 14, 3, 0, 14, 3, 0, 14, 0]
total_cost = 226

# Verify the given solution
result = verify_solution(tour, total_cost)
print(result)