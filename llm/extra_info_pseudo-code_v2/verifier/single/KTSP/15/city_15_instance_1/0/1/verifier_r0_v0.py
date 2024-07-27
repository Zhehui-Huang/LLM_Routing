import math

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def verify_solution(tour, total_cost):
    cities = {
        0: (29, 51),
        1: (49, 20),
        2: (79, 69),
        3: (17, 20),
        4: (18, 61),
        5: (40, 57),
        6: (57, 30),
        7: (36, 12),
        8: (93, 43),
        9: (17, 36),
        10: (4, 60),
        11: (78, 82),
        12: (83, 96),
        13: (60, 50),
        14: (98, 1)
    }
    
    # [Requirement 1] Check if the robot starts and ends at depot city 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # [Requirement 2] Check if exactly 6 cities are visited including the depot
    if len(tour) != 7:
        return "FAIL"
    
    # [Requirement 3] This is inherently satisfied as all pairs can be direct neighbors
    
    # [Requirement 4] Check total travel cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"
    
    # [Requirement 6] Ensure output format correctness (implicit in parameters of this function)
    return "CORRECT"

# Test input
tour = [0, 10, 4, 11, 13, 1, 0]
total_cost = 209.74

# Verify if the solution is correct
result = verify_solution(tour, total_selection_cost)
print(result)