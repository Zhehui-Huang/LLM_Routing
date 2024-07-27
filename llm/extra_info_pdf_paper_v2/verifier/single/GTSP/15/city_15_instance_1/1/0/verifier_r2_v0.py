import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_cost):
    # City coordinates
    coordinates = {
        0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
        5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
        10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
    }
    
    # Group definitions
    groups = {
        0: [1, 2, 5, 6],
        1: [8, 9, 10, 13],
        2: [3, 4, 7],
        3: [11, 12, 14]
    }

    # Check Requirement 1: Tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: Exactly one city from each group
    visited_groups = [False] * 4
    for city in tour[1:-1]:  # Exclude depot (start/end)
        for i, group in groups.items():
            if city in group:
                if visited_groups[i]:
                    return "FAIL"
                visited_groups[i] = True
                break
    
    if not all(visited_groups):
        return "FAIL"
    
    # Check Requirement 3 & 5: Correct travel cost calculation and output
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i+1]
        calculated_cost += calculate_euclidean_distance(*coordinates[city1], *coordinates[city2])
    
    if abs(calculated_cost - total_cost) > 0.01:
        return "FAIL"
    
    return "CORRECT"

# Given solution
tour = [0, 5, 10, 4, 11, 0]
reported_total_cost = 184.24

# Verification
result = verify_solution(tour, reported_total_cost)
print(result)