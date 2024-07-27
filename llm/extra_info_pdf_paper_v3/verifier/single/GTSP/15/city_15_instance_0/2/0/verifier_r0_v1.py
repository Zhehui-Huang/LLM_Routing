import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, cities, groups):
    # Verify tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify one city from each group is visited
    visited_groups = set()
    for city_index in tour[1:-1]:  # Exclude the depot city at the start and end
        found_group = False
        for group_index, group in enumerate(groups):
            if city_index in group:
                if group_index in visited_groups:
                    return "FAIL"
                else:
                    visited_groups.add(group_index)
                    found_group = True
                    break
        if not found_group:
            return "FAIL"
                
    if len(visited_groups) != len(groups):
        return "FAIL"

    # Verify the total cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    if not math.isclose(calculated_cost, total_cost, abs_tol=0.1):
        return "FAIL"
    
    return "CORRECT"

# Test the provided solution
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
          (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]
groups = [[2, 7, 10, 11, 14], [1, 3, 5, 8, 13], [4, 6, 9, 12]]

# Proposed solution
tour = [0, 10, 1, 9, 0]
total_cost = 122.22

# Validate the solution
print(verify_solution(tour, total_cost, cities, groups))