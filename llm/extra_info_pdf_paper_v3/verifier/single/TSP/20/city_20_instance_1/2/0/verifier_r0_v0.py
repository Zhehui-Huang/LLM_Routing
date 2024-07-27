import math

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def verify_solution(tour, total_cost, cities_coordinates):
    requirements_met = True
    tour_cost_calculated = 0
    
    # [Requirement 1] Check start and end at the depot city (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        requirements_met = False
    
    # [Requirement 2] Check if all cities are visited exactly once
    all_cities_visited = set(range(1, 20))  # From city 1 to 19
    cities_in_tour = set(tour[1:-1])  # Exclude starting and ending depot city
    if cities_in_tour != all_cities_visited:
        requirements_met = False
    
    # [Requirement 3] Compute the total travel cost using the Euclidean distance
    for i in range(1, len(tour)):
        city_a_index = tour[i - 1]
        city_b_index = tour[i]
        tour_cost_calculated += euclidean_distance(cities_coordinates[city_a_index], cities_coordinates[city_b_index])
    
    # Allowing a small precision error due to floating point operations
    if not math.isclose(tour_cost_calculated, total_cost, rel_tol=1e-9):
        requirements_met = False
    
    return "CORRECT" if requirements_met else "FAIL"

# Coordinates of the cities including the depot city
cities_coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Provided solution to verify
tour_solution = [0, 6, 2, 9, 13, 12, 8, 1, 15, 19, 18, 17, 11, 10, 16, 4, 7, 5, 14, 3, 0]
total_cost_solution = 405.1098708113318

# Verify the solution
result = verify_solution(tour_solution, total_cost_solution, cities_coordinates)
print(result)