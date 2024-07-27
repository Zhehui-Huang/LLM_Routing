import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost, cities, groups):
    # Requirement 1: The robot must start and end its tour at depot city, which is city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: The robot must visit exactly one city from each of the six specified groups of cities.
    visited_groups = [False] * len(groups)
    for city in tour[1:-1]:  # Exclude the depot city at start and end
        found_group = False
        for i, group in enumerate(groups):
            if city in group:
                if visited_groups[i]:
                    return "FAIL"  # City from the same group visited more than once
                visited_groups[i] = True
                found_group = True
                break
        if not found_group:
            return "FAIL"
    
    if not all(visited_groups):
        return "FAIL"
    
    # Requirement 3: The total travel cost is calculated as the sum of the Euclidean distances between consecutive cities in the tour.
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_mobile_distance(tour[i], tour[i + 1])
    
    if not math.isclose(calculated_cost, total_cost, abs_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Data used in the test
cities = [
    (84, 67),  # Depot city 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

groups = [
    [7, 9],   # Group 0
    [1, 3],   # Group 1
    [4, 6],   # Group 2
    [8],      # Group 3
    [5],      # Group 4
    [2]       # Group 5
]

# Given tour and cost from solution
tour = [0, 7, 1, 4, 8, 5, 2, 0]
total_cost = 324.1817486177585

def euclidean_mobile_distance(city_index1, city_index2):
    return euclidean_distance(cities[city_index1], cities[city_filter2])

# Verifying the solution
result = verify_solution(tour, total_cost, cities, groups)
print(result)