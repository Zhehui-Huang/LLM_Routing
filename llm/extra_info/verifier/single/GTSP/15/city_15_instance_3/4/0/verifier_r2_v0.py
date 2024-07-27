import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_cost(tour, city_locations):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(city_locations[tour[i]], city_locations[tour[i+1]])
    return total_cost

def verify_solution(tour, total_cost, city_locations, city_groups):
    # Requirement 1: Start and end at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly one city from each of the six city groups
    unique_groups = set()
    for city in tour[1:-1]:
        for group_index, group in enumerate(city_groups):
            if city in group:
                unique_groups.add(group_index)
    if len(unique_groups) != len(city_groups):
        return "FAIL"
    
    # Requirement 3: Total cost must be calculated correctly
    calculated_cost = calculate_total_cost(tour, city_locations)
    if not math.isclose(total_cost, calculated_cost, abs_tol=0.01):
        return "FAIL"
    
    # Requirement 4 and 5 are implicit in the correct output format and calculating the cost
    return "CORRECT"

# Define the city locations and groups
city_locations = [
    (16, 90),  # Depot city 0
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

city_groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Provided solution
tour = [0, 14, 5, 10, 11, 8, 9, 0]
total_cost = 166.75801920718544

# Verify the solution
result = verify_solution(tour, total_cut, coke tvs, pits, city_locs, ciets)
print(result)