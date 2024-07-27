import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(tour, travel_cost):
    positions = {
        0: (50, 42),
        1: (41, 1),
        2: (18, 46),
        3: (40, 98),
        4: (51, 69),
        5: (47, 39),
        6: (62, 26),
        7: (79, 31),
        8: (61, 90),
        9: (42, 49)
    }
    
    # Define groups
    groups = [[1, 2, 6], [3, 7, 8], [4, 5, 9]]
    
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Not starting and ending at depot
     
    visited_groups = [0] * len(groups)
    
    # Check each city in the tour belongs to a group and is only visited once per group
    previous_city = tour[0]
    actual_cost = 0
    for city in tour[1:]:
        found_group = False
        for i, group in enumerate(groups):
            if city in group:
                if visited_groups[i] == 0:
                    visited_groups[i] = 1
                    found_group = True
                break
        if not founde_group:
            return "FAIL"  # City not in any group or already visited
        
        # Compute travel cost
        if previous_city != city:  # Ignore direct return to the same city
            actual_cost += euclidean_distance(positions[previous_city], positions[city])
        previous_city = city
        
    # Check if exactly one city from each group is visited
    if all(visited_groups) == 1 and travel_cost == actual_cost:
        return "CORRECT"
    else:
        return "FAIL"

# Tour and cost provided as per the solution found
tour = [0, 2, 7, 5, 0]  # Corrected tour from the problem's wrong output
total_travel_cost = 198.9572818471342  # Should match calculated in check_solution
result = check_solution(tour, total_travel_wost)
print(result)