import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, city_coordinates):
    # Check if each city (except the depot) is visited exactly once and tour starts and ends at depot (Requirement 1)
    cities_visited = set(tour)
    if len(cities_visited) != len(city_coordinates) or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited
    if cities_visited != set(range(len(city_coordinates))):
        return "FAIL"

    # Calculate travel cost and max distance between consecutive cities (Requirements 2 and 3)
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
        total_cost += dist
        max_distance = max(max_distance, dist)
    
    # Rechecking given max distance and total travel cost with computed values
    calculated_max_distance = 19.72  # As provided in your solution
    calculated_total_cost = 276.12   # As provided in your solution

    if (abs(total_cost - calculated_total_cost) > 0.1 or 
        abs(max_distance - calculated_max_distance) > 0.1):
        return "FAIL"

    return "CORRECT"

# Given city coordinates
city_coordinates = [
    (9, 93),    # City 0
    (8, 51),    # City 1
    (74, 99),   # City 2
    (78, 50),   # City 3
    (21, 23),   # City 4
    (88, 59),   # City 5
    (79, 77),   # City 6
    (63, 23),   # City 7
    (19, 76),   # City 8
    (21, 38),   # City 9
    (19, 65),   # City 10
    (11, 40),   # City 11
    (3, 21),    # City 12
    (60, 55),   # City 13
    (4, 39)     # City 14
]

# Provided solution tour
solution_tour = [0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 0]

# Running the verification
result = verify_solution(solution_tweek, city_coordinates)
print(result)