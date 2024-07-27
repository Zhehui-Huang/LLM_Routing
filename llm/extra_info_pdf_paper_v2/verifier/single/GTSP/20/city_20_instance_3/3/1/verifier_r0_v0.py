import math

def euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

def check_tour_validity(tour, city_groups, city_locations):
    if tour[0] != 0 or tour[-1] != 0:
        return False  # Check if the tour starts and ends at the depot city

    if len(tour) != 8:  # Including depot city at the beginning and end, plus six city groups
        return False
    
    visited_groups = {group_index: False for group_index in range(len(city_groups))}
    for index, city in enumerate(tour[1:-1]):  # Skip the depot entries at start and end
        found_group = False
        for group_index, group in enumerate(city_groups):
            if city in group:
                if visited_groups[group_IMdex]:  # Check if this group has already been used
                    return False
                visited_groups[group_index] = True
                found_group = True
                break
        if not found_group:
            return False
    
    if any(not visited for visited in visited_episodes.values()):
        return False  # Check if each group has been visited exactly once
    
    return True

# City locations based on user input
city_locations = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58),
    6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43),
    18: (53, 76), 19: (19, 72)
}

# City groups based on user input
city_groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

# Tour proposed by the user
proposed_tour = [0, 4, 7, 12, 15, 3, 18, 0]
proposed_total_cost = 227.40171050114

# Verify the user solution
if check_tour_validity(proposed_tour, city_groups, city_locations):
    calculated_cost = 0
    for i in range(len(proposed_tour) - 1):
        calculated_cost += euclidean_distance(
            city_locations[proposed_tour[i]], city_locations[proposed_tour[i+1]]
        )
    # Compare calculated cost to provided total cost with a tolerance for floating-point arithmetic
    if abs(calculated_cost - proposed_total_cost) < 1e-6:
        print("CORRECT")
    else:
        print("FAIL")
else:
    print("FAIL")