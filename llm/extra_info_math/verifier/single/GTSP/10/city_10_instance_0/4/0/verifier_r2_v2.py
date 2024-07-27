import math

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities given their coordinates. """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(tour, travel_cost):
    """ Verify if the provided tour and cost satisfy the requirements. """
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
    
    # Group assignments
    groups = [[1, 2, 6], [3, 7, 8], [4, 5, 9]]
    
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Must start and end at the depot city 0
    
    visited_groups = [0] * len(groups)
    actual_cost = 0
    previous_city = tour[0]
    
    for city in tour[1:]:
        found_group = False
        for group_index, group in enumerate(groups):
            if city in group:
                if visited_groups[group_index] == 0:
                    visited_groups[group_index] = 1
                    found_group = True
                    break
        if not found_group:
            return "FAIL"  # City must be part of a group and not visited more than once
        
        # Calculate distance and accumulate travel cost
        actual_cost += euclidean_distance(positionedits[previous_city], positions[city])
        previous_city = city
    
    if all(visited_groups) and math.isclose(actual_cost, travel_cost, rel_tol=1e-9):
        return "CORRECT"
    else:
        return "FAIL"

# Defined tour and travel cost
tour = [0, 2, 7, 5, 0]
total_travel_cost = 198.9572818471342

# Testing the solution
result = check_solution(tour, total_travel_cost)
print(result)