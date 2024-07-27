import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, total_travel_cost):
    city_coordinates = [
        (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
        (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
        (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
        (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
    ]
    
    city_groups = [
        [7, 10, 11, 12], [3, 8, 13, 16], [2, 4, 15, 18], 
        [1, 9, 14, 19], [5, 6, 17]
    ]
    
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Tour must start and end at the depot city
    
    visited_groups = set()
    for i in range(1, len(tour) - 1):  # Exclude the depot (start and end)
        found_group = False
        for group_index, group in enumerate(city_groups):
            if tour[i] in group:
                if group_index in visited_groups:
                    return "FAIL"  # City from the same group visited more than once
                visited_groups.add(group_index)
                found_group = True
                break
        if not found_group:
            return "FAIL"  # City in tour not found in any group
    
    if len(visited_groups) != len(city_groups):
        return "FAIL"  # Not all groups are visited
    
    # Validate travel cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = city_coordinates[tour[i]]
        x2, y2 = city_coordinates[tour[i + 1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"  # Calculated total travel cost does not match the provided cost
    
    return "CORRECT"

# Test the provided example
test_tour = [0, 12, 16, 18, 19, 6, 0]
test_total_travel_cost = 173.05943990280707
result = verify_tour(test_tour, test_total_travel_cost)
print(result)