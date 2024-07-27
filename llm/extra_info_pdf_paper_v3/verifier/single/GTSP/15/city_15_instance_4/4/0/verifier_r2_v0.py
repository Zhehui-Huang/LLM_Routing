import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def validate_solution(tour, cost):
    coordinates = [
        (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
        (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), 
        (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
    ]
    
    city_groups = [
        [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
    ]
    
    # Requirement 1: Start and end at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly one city from each group
    visited_groups = set()
    for city in tour[1:-1]:  # exclude the depot at start and end
        for idx, group in enumerate(city_groups):
            if city in group:
                if idx in visited_groups:
                    return "FAIL"
                visited_groups.add(idx)
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Requirement 3: Correct travel cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    if abs(calculated_cost - cost) > 0.01:  # Allowing a small margin for float comparisons
        return "FAIL"
    
    # Requirement 4: Proper output format checked by passing output directly
    return "CORRECT"

# Given solution evaluation
tour_given = [0, 8, 13, 1, 14, 5, 12, 11, 0]
cost_given = 220.73

# Validate and output the result
print(validate_solution(tour_given, cost_given))