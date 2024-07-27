import math

# Given data
cities = {
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

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(tour, total_travel_cost, max_distance):
    # Check requirement 1: Visit each city exactly once, starting and ending at the depot city
    if len(tour) != len(cities) + 1:
        return "FAIL"
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if len(set(tour)) != len(cities) + 1:
        return "FAIL"
    
    # Calculate travel cost and verify maximum distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i+1]
        distance = calculate_distance(cities[city1], cities[city2])
        calculated_total_cost += distance
        calculated_max_distance = max(calculated_max_distance, distance)
    
    # Check requirement 2 and 3: Minimize the longest distance, correct tour, and total cost
    if abs(calculated_total_cost - total_travel_input) > 1e-5:
        return "FAIL"
    if abs(calculated_max_distance - max_distance) > 1e-5:
        return "FAIL"
    
    return "CORRECT"

# Given solution
tour = [0, 2, 4, 3, 8, 9, 7, 5, 1, 6, 0]
total_travel_input = 336.4015755047926
max_distance_input = 45.18849411078001

# Verify and print result
result = check_solution(tour, total_travel_input, max_distance_input)
print(result)