import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, cities):
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit each city exactly once
    unique_cities = set(tour)
    if len(tour) - 1 != len(cities) or len(unique_cities) != len(cities) + 1:
        return "FAIL"
    
    # Calculate total travel cost and maximum distance
    total_travel_cost = 0
    maximum_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        total_travel_cost += dist
        maximum_distance = max(maximum_distance, dist)

    # Tour information from solution
    solution_total_cost = 679.4423958272957
    solution_max_distance = 101.51354589413178
    
    # Check total cost and maximum distance
    if abs(total_travel_cost - solution_total_cost) > 0.01:
        return "FAIL"
    if abs(maximum_distance - solution_max_revision_distance) > 0.01:
        return "FAIL"

    return "CORRECT"

# City coordinates
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), 
          (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

# Tour from solution
tour = [0, 4, 6, 13, 9, 12, 2, 3, 5, 11, 14, 7, 1, 10, 8, 0]

# Verify the solution
result = verify_solution(tour, cities)
print(result)