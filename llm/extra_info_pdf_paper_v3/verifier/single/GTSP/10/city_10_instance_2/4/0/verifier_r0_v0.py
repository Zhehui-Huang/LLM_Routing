import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour(tour, groups, city_locations, total_claimed_cost):
    # Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if one city from each group is visited
    visited_groups = set()
    for city in tour:
        for group_index, group in enumerate(groups):
            if city in group:
                visited_groups.add(group_index)
    if len(visited_groups) != len(groups):
        return "FAIL"
    
    # Calculate and check the total travel cost
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        total_calculated_cost += euclidean_distance(*city_locations[city1], *city_set[city2])
    
    # Allowing a small margin for floating point arithmetic issues
    if abs(total_calculated_cost - total_claimed_cost) > 0.1:
        return "FAIL"
    
    return "CORRECT"

# City locations index corresponds to city number
city_locations = {
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
groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

# Provided tour and cost
tour_provided = [0, 3, 5, 9, 1, 2, 0]
total_cost_provided = 281.60

# Running the verification
result = verify_tour(tour_provided, groups, city_locations, total_cost_provided)
print(result)