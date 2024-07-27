import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(cities, tour, expected_total_cost, expected_max_distance):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Tour must start and end at city 0
    
    if len(set(tour)) != len(cities):
        return "FAIL"  # All cities must be present exactly once in the tour, including the depot
    
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        city_index_from = tour[i]
        city_index_to = tour[i + 1]
        distance = euclidean_distance(cities[city_index_from], cities[city_index_to])
        total_cost += distance
        max_distance = max(max_distance, distance)
    
    # Check if sum of distances and max distance match expected values
    if not math.isclose(total_cost, expected_total_cost, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(max_distance, expected_max_distance, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Given cities and their position
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23), 6: (97, 32),
    7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25),
    14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Solution output
tour = [0, 4, 15, 13, 7, 10, 8, 12, 14, 17, 3, 11, 2, 18, 6, 5, 16, 9, 1, 0]
total_travel_cost = 377.7115620630163
maximum_distance = 32.38826948140329

# Verify the solution's correctness
print(verify_solution(cities, tour, total_travel_cost, maximum_distance))