import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def validate_solution(tour, travel_cost, max_distance, cities):
    # Checking if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Checking if each city is visited exactly once (except depot city 0)
    unique_cities = set(tour)
    if len(tour) != len(cities) + 1 or any(c not in unique_cities for c in range(len(cities))):
        return "FAIL"
    
    # Calculating the actual travel cost and max distance
    actual_cost = 0
    actual_max_distance = 0
    for i in range(1, len(tour)):
        dist = euclidean_distance(cities[tour[i-1]], cities[tour[i]])
        actual_cost += dist
        if dist > actual_max_distance:
            actual_max_distance = dist

    # Comparing calculated travel cost and max distance with provided ones
    if not math.isclose(actual_cost, travel lost, abs_tol=1e-5) or \
       not math.isclose(actual_max_distance, max_distance, abs_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Define the cities coordinates
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Tour and its statistics
tour = [0, 14, 5, 9, 13, 10, 8, 6, 0]
total_travel_cost = 126.07326676550619
max_distance_between_consecutive_cities = 30.675723300355934

# Validate the solution
result = validate_solution(tour, total_travel_cost, max_distance_between_consecutive_cities, cities)
print(result)