import math

def compute_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def verify_solution(tour, total_cost):
    # City coordinates
    cities = {
        0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
        5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
        10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
    }
    
    # Group assignments
    groups = [
        [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
    ]
    
    # Check Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2: Visit exactly one city from each group
    visited_groups = [False] * len(groups)
    for city in tour[1:-1]:  # Exclude the depot city at start and end
        is_in_group = False
        for i, group in enumerate(groups):
            if city in group:
                if visited_groups[i]:
                    return "FAIL"  # City from the same group visited more than once
                visited_groups[i] = True
                is_in_group = True
                break
        if not is_in_group:
            return "FAIL"  # City is not in any group
    if not all(visited_groups):
        return "FAIL"  # Not all groups are visited
    
    # Check Requirement 3 & 6: Correct distance calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        start_city = tour[i]
        end_city = tour[i + 1]
        calculated_cost += compute_euclidean_distance(*cities[start_city], *cities[end_city])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"  # Total cost does not match the expected cost

    # Check Requirement 4, 5 are implicit in other checks
    
    return "CORRECT"

# Given test solution
tour = [0, 13, 14, 8, 11, 12, 5, 1, 0]
total_cost = 156.56

# Validate the tour and cost
result = verify_solution(tour, total_cost)
print(result)  # Should output "CORRECT" if the solution is correct otherwise "FAIL"