import math

def euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

def check_solution(tour, cost, cities, groups):
    # Check if the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited_groups = {}
    for city_index in tour[1:-1]:  # exclude the depot city at start and end
        for group_index, group in enumerate(groups):
            if city_index in group:
                if group_index in visited_groups:
                    return "FAIL"
                else:
                    visited_groups[group_index] = True
    if len(visited_groups) != len(groups):
        return "FAIL"

    # Check total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(cost, calculated_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Data from the problem
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68),
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), 
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

groups = [
    [7, 10, 11, 12], # Group 0
    [3, 8, 13, 16],  # Group 1
    [2, 4, 15, 18],  # Group 2
    [1, 9, 14, 19],  # Group 3
    [5, 6, 17]        # Group 4
]

tour = [0, 6, 14, 16, 18, 12, 0]
total_cost = 170.22489356581875

# Use the check_solution function to validate the provided solution
result = check_solution(tour, total_cost, cities, groups)
print(result)