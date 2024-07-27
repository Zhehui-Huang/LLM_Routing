import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_solution(tour, city_coordinates, total_travel_cost, max_distance):
    # Requirement 1: Check if each city is visited exactly once and starts/ends at depot
    if sorted(tour) != [0] + sorted(tour[1:-1]) or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate distances and verify against provided costs
    computed_total_cost = 0
    computed_max_distance = 0
    
    for i in range(1, len(tour)):
        distance = calculate_distance(city_coordinates[tour[i-1]], city_coordinates[tour[i]])
        computed_total_cost += distance
        if distance > computed_max_distance:
            computed_max_distance = distance
    
    # Requirement 2: Total cost and maximum distance verification
    if not math.isclose(computed_total_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(computed_max_distance, max_distance, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# City Coordinates
city_coordinates = [
    (90, 3),  
    (11, 17),  
    (7, 27),  
    (95, 81),  
    (41, 54),  
    (31, 35),  
    (23, 95),  
    (20, 56),  
    (49, 29),  
    (13, 17)   
]

# Provided Solution Details
tour = [0, 5, 1, 2, 9, 7, 6, 4, 3, 8, 0]
total_travel_cost = 418.32344417340323
maximum_distance = 69.42621983083913

# Verify the solution
print(verify_solution(tour, city_coordinates, total_travel_cap, type_maximum_distance))