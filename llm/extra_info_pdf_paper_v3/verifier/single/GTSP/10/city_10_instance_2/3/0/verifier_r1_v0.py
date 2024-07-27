import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def check_requirements(solution_tour, total_cost):
    # City coordinates
    coords = {
        0: (90, 3),
        1: (11, 17),
        2: (7, 27),
        3: (95, 81),
        4: (41, 54),
        5: (31, 35),
        6: (23, 95),
        7: (20, 56),
        8: (49, 29),
        9: (13, 17)
    }
    
    # City groups
    city_groups = {
        0: [3, 6],
        1: [5, 8],
        2: [4, 9],
        3: [1, 7],
        4: [2]
    }
    
    # [Requirement 3] Verify tour starts and ends at the depot city 0
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2 & 5] Check one city from each group is visited
    visited_groups = {k: False for k in city_groups.keys()}
    
    for city in solution_tour[1:-1]:  # skipping starting and ending depot
        for group, cities in city_groups.items():
            if city in cities:
                if visited_groups[group]:
                    return "FAIL"  # more than one city from a group visited
                visited_groups[group] = True
                break
    
    if not all(visited_groups.values()):
        return "FAIL"
    
    # [Requirement 4 & 6] Check the travel cost calculation
    calculated_cost = 0
    for i in range(len(solution_tour) - 1):
        calculated_cost += euclidean_distance(coords[solution_tour[i]], coords[solution_tour[i+1]])
    
    if abs(calculated_cost - total_cost) > 1e-5:  # allowing floating-point error tolerance
        return "FAIL"
    
    # If all checks are passed
    return "CORRECT"

# Given solution
tour = [0, 3, 5, 9, 1, 2, 0]
total_travel_cost = 281.60273931778477

# Verification execution
result = check_requirements(tour, total_travel_cost)
print(result)