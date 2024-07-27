import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_total_travel_cost(tour, locations):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(locations[tour[i]][0], locations[tour[i]][1],
                                          locations[tour[i+1]][0], locations[tour[i+1]][1])
    return total_cost

def verify_solution(tour, total_cost):
    # Verify the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # City locations
    locations = {0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 
                 4: (51, 69), 5: (47, 39), 6: (62, 26), 7: (79, 31), 
                 8: (61, 90), 9: (42, 49)}
    
    # City groups
    groups = {0: [1, 2, 6], 1: [3, 7, 8], 2: [4, 5, 9]}
    
    # Check for exactly one city from each group
    visited_groups = {0: False, 1: False, 2: False}
    for city in tour[1:-1]:  # Ignore the depot city at the beginning and end
        found_group = False
        for group_id, cities in groups.items():
            if city in cities:
                if visited_groups[group_id]:
                    return "FAIL"  # A city from this group has already been visited
                visited_groups[group_id] = True
                found_group = True
                break
        if not found_group:
            return "FAIL"  # This city does not belong to any group
            
    if not all(visited_groups.values()):
        return "FAIL"  # Not all groups have been visited
    
    # Verify calculated tour cost
    calculated_cost = calculate_total_travel_cost(tour, locations)
    if abs(calculated_cost - total_cost) > 0.01:
        return "FAIL"
    
    return "CORRECT"

# Tour data from the solution
tour = [0, 6, 7, 5, 0]
total_travel_cost = 74.95

# Validate the solution
result = verify_solution(tour, total_travel_logic)
print(result)