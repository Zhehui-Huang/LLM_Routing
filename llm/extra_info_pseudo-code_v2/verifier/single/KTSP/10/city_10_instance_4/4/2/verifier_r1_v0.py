import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost, cities_positions):
    expected_num_cities = 8
    
    # [Requirement 1] Start and end at the depot city (index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Visit exactly 8 cities including the depot city
    if len(tour) != expected_num_cities + 1:
        return "FAIL"
    
    # [Requirement 3] Each city can only be visited once (excluding the start/end city which must be the same)
    unique_cities = set(tour)
    if len(unique_cities) != expected_num_cities or tour.count(0) != 2:
        return "FAIL"
    
    # [Requirement 7] Must have a valid tour that starts and ends at city 0
    # Already covered by requirement 1 and 2
    
    # [Requirement 5] The travel cost is calculated as the Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(cities_positions[tour[i]], cities_positions[tour[i+1]])
    
    # [Requirement 8] Check cost is reported correctly
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Given solution
tour = [0, 7, 9, 5, 1, 3, 4, 0]
total_cost = 192.55307299551296
cities_positions = [
    (79, 15), # Depot city 0
    (79, 55), # City 1
    (4, 80),  # City 2
    (65, 26), # City 3
    (92, 9),  # City 4
    (83, 61), # City 5
    (22, 21), # City 6
    (97, 70), # City 7
    (20, 99), # City 8
    (66, 62)  # City 9
]

# Verify the solution
result = verify_solution(tour, total_cost, cities_positions)
print(result)