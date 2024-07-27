import math

# Given city coordinates
city_coordinates = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Solution info
tour = [0, 4, 3, 1, 5, 7, 9, 8, 2, 6, 0]
reported_cost = 337.17

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour(tour, reported_cost):
    # Check start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check all cities visited once
    visited = set(tour[1:-1])
    if not all(city in visited for city in range(1, len(city_coordinates))) or len(visited) != len(city_coordinates) - 1:
        return "FAIL"
    
    # Calculate and check total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    # Compare computed total cost with reported cost
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-2):  # with a small tolerance for floating point errors
        return "FAIL"
    
    return "CORRECT"

# Output the verification result
print(verify_tour(tour, reported_cost))