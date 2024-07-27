import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_tsp_solution(tour, total_cost, cities_coordinates):
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if the robot visits exactly 4 cities
    if len(set(tour)) != 5:  # +1 because the starting city 0 is counted twice
        return "FAIL"
    
    # Check if the tour length according to Euclidean distance is calculated correctly
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Given data
cities_coordinates = [
    (8, 11),  # Depot city 0
    (40, 6),  # City 1
    (95, 33), # City 2
    (80, 60), # City 3
    (25, 18), # City 4
    (67, 23), # City 5
    (97, 32), # City 6
    (25, 71), # City 7
    (61, 16), # City 8
    (27, 91), # City 9
    (91, 46), # City 10
    (40, 87), # City 11
    (20, 97), # City 12
    (61, 25), # City 13
    (5, 59),  # City 14
    (62, 88), # City 15
    (13, 43), # City 16
    (61, 28), # City 17
    (60, 63), # City 18
    (93, 15)  # City 19
]

proposed_tour = [0, 1, 8, 4, 0]
proposed_total_cost = 110.08796524611944

# Validation
result = check_tsp_solution(proposed_tour, proposed_total_cost, cities_coordinates)
print(result)