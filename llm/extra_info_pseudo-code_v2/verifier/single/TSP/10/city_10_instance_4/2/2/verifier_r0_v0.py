import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_cost):
    # Given city coordinates matching the problem statement
    coordinates = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9),
                   (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]
    
    # Requirement 4
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 1
    visited = set(tour)
    if len(tour) != len(coordinates) + 1 or len(visited) != len(coordinates):
        return "FAIL"
    
    # Requirement 2 & Requirement 5
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    
    # Requirement 5 - using a tolerance due to floating-point arithmetic inaccuracies
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Given solution
tour = [0, 4, 3, 1, 5, 7, 9, 8, 2, 6, 0]
total_cost = 337.1694332678818

# Verify the solution
result = verify_solution(tour, total_cost)
print(result)