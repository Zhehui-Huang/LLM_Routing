import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tour, cities, total_travel_cost, max_distance):
    # Check Requirement 1: Visit each city exactly once and return to the starting city
    if len(tour) != len(cities) + 1 or tour[0] != tour[-1] or len(set(tour[:-1])) != len(cities):
        return "FAIL"

    # Calculate travel cost and check maximum distance
    calculated_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_cost += distance
        if distance > calculated_max_distance:
            calculated_max_istance = distance

    # Match computed and given costs and maximum distance
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-2):
        return "FAIL"
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# City coordinates, 0-indexed according to problem statement
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59),
    6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65), 
    11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Tour and costs provided
tour = [0, 8, 10, 1, 11, 14, 9, 12, 4, 7, 3, 5, 13, 6, 2, 0]
total_travel_cost = 358.43
maximum_distance = 42.00

# Verify solution
result = verify_solution(tour, cities, total_travel_cost, maximum_distance)
print(result)