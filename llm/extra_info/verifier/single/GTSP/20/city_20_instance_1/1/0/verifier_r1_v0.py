import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, city_positions, city_groups):
    # Requirement 1: Starts and ends at depot city, index 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visits exactly one city from each group
    visited_groups = set()
    for city in tour[1:-1]:
        for index, group in enumerate(city_groups):
            if city in group:
                visited_groups.add(index)
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Requirement 3: Calculate total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(city_positions[tour[i]], city_positions[tour[i+1]])
    
    # Requirement 6: Check the correctness of the provided total travel cost
    if not math.isclose(calculated_cost, total_cost, abs_tol=0.01):
        return "FAIL"
    
    # Requirement 4 and 5 are conceptual and not directly testable without solving the problem anew
    return "CORRECT"

# City coordinates
city_positions = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), 
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45), 
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), 
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Group assignments
city_groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Solution to check
solution_tour = [0, 6, 13, 2, 9, 0]
claimed_total_cost = 114.66

# Verify the provided solution
result = verify_solution(solution_tour, claimed_total_cost, city_positions, city_groups)
print(result)