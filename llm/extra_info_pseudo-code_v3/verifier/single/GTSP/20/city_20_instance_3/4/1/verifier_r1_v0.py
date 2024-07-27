import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City coordinates indexed by city number
city_coords = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# City groups
city_groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

# Proposed tour and its cost
proposed_tour = [0, 19, 6, 2, 13, 12, 18, 0]
proposed_cost = 158.65862319241174

def verify_tour():
    # Check if the tour starts and ends at the depot city 0
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each group is visited
    visited_groups = [0] * len(city_groups)
    for city in proposed_tour[1:-1]:
        group_found = False
        for i, group in enumerate(city_groups):
            if city in group:
                visited_groups[i] += 1
                group_found = True
                break
        if not group_found or visited_groups[i] > 1:
            return "FAIL"
    
    if any(v != 1 for v in visited_groups):
        return "FAIL"

    # Check total travel cost
    calculated_cost = 0
    for i in range(len(proposed_tour) - 1):
        start = proposed_tour[i]
        end = proposed_tour[i + 1]
        calculated_cost += euclidean_distance(city_coords[start], city_coords[end])
    
    if abs(calculated_cost - proposed_cost) > 1e-5:
        return "FAIL"
    
    return "CORRECT"

# Output the result
print(verify_tour())