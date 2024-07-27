import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_tour(tour, total_cost):
    # City coordinates
    cities = {
        0: (3, 26),
        1: (85, 72),
        2: (67, 0),
        3: (50, 99),
        4: (61, 89),
        5: (91, 56),
        6: (2, 65),
        7: (38, 68),
        8: (3, 92),
        9: (59, 8),
        10: (30, 88),
        11: (30, 53),
        12: (11, 14),
        13: (52, 49),
        14: (18, 49),
        15: (64, 41),
        16: (28, 49),
        17: (91, 94),
        18: (51, 58),
        19: (30, 48)
    }

    # Groups of cities
    groups = [
        {7, 10, 11, 12},
        {3, 8, 13, 16},
        {2, 4, 15, 18},
        {1, 9, 14, 19},
        {5, 6, 17}
    ]
    
    # Check if the tour starts and ends at the depot (Requirement 1 and Requirement 4)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if one city from each group is visited exactly once (Requirement 2)
    visited_groups = [0] * len(groups)
    for city in tour[1:-1]:  # Exclude the depot city at start and end
        for group_id, group in enumerate(groups):
            if city in group:
                visited_groups[group_id] += 1
                
    if any(count != 1 for count in visited_groups):
        return "FAIL"
    
    # Calculate travel cost and compare with given total cost (Requirement 3 and Requirement 4)
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += euclidean_distance(*cities[city1], *cities[city2])
    
    if abs(calculated_cost - total_cost) > 1e-6:
        return "FAIL"
    
    # Requirement 5 is always satisfied given the problem setup
    return "CORRECT"

# Given solution
tour = [0, 13, 18, 11, 14, 6, 0]
total_cost = 159.0612387388631

# Test the given solution
result = validate_tour(tour, total_cost)
print(result)