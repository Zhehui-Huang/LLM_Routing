def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)**0.5

def verify_solution(tour, city_positions, groups):
    # Check if the robot starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if the robot visits exactly one city from each group
    visited_cities = tour[1:-1]  # remove the depot city from the start and end
    visited_groups = set()
    for city in visited_cities:
        for i, group in enumerate(groups):
            if city in group:
                if i in visited_groups:
                    return "FAIL"  # city from the same group visited more than once
                visited_groups.add(i)
    if len(visited_groups) != len(groups):
        return "FAIL"  # not all groups were visited
    
    # Check the total travel cost (should be minimal, suboptimal solutions are not detectable here without global comparison)
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(city_positions[tour[i]], city_positions[tour[i + 1]])
    if total_cost != 291.29:  # the reported cost must match
        return "FAIL"

    return "CORRECT"

# Values based on problem specification
city_positions = [
    (90, 3),  # Depot city 0
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
]

# Groups
groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

# Solution Tour and Cost Provided
solution_tour = [0, 8, 0, 8, 0, 8, 0]

# Verify and output the result
print(verify_solution(solution_tour, city_positions, groups))