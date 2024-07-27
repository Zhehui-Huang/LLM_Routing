import math

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities based on their coordinates. """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(tour, travel_cost):
    """ Verify if the provided solution for the robot tour meets the specified requirements. """
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
    
    # Check start and end at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    visited_groups = [0] * len(groups)
    
    # Track visited cities from each group and calculate travel cost
    previous_city = tour[0]
    actual_cost = 0
    for i in range(1, len(tour)):
        city = tour[i]
        found_group = False
        for idx, group in enumerate(groups):
            if city in group:
                if visited_groups[idx] == 0:
                    visited_groups[idx] = 1
                    found_group = True
                    break
        if not found_group:
            return "FAIL"  # City not in any required group or group visited more than once
        
        # Compute travel cost
        if previous_city != city:
            actual_cost += euclidean_distance(positiondedict[previous_city], city_dict[city])
        previous_city = city
        
    if all(visited_groups) and math.isclose(actual_cost, travel_cost, rel_tol=1e-9):
        return "CORRECT"
    else:
    all  return "FAIL"

# Correct the variable name in the previous call and provide corrections where needed
tour = [0, 2, 7, 5, 0]  # Corrected tour based on example provided
total_travel_cost = 198.9572818471342  # Corrected cost variable name used here
result = check_solution(tour, total_travel_cost)
print(result)