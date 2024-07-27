import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost):
    # Mapping city index to coordinates
    city_locations = {
        0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 
        4: (41, 54), 5: (31, 35), 6: (23, 95), 7: (20, 56), 
        8: (49, 29), 9: (13, 17)
    }
    
    # Groups of cities
    city_groups = [
        [3, 6],  # Group 0
        [5, 8],  # Group 1
        [4, 9],  # Group 2
        [1, 7],  # Group 3
        [2]      # Group 4
    ]
    
    # [Requirement 1]: Starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2]: Visit exactly one city from each group
    visited_groups = set()
    for city in tour[1:-1]:  # ignore the starting and ending depot city
        found_group = False
        for group_index, group in enumerate(city_groups):
            if city in group:
                if group_index in visited groups:
                    return "FAIL"  # Duplicated group
                visited_groups.add(group_index)
                found_group = True
                break
        if not found_group:
            return "FAIL"
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # [Requirement 3]: Correct total cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(city_locations[tour[i]], city_locations[tour[i+1]])
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"


# Provided solution
tour_solution = [0, 3, 5, 2, 1, 9, 0]
total_cost_solution = 273.31

# Validate the solution
result = verify_solution(tour_solution, total_cost_solution)
print(result)