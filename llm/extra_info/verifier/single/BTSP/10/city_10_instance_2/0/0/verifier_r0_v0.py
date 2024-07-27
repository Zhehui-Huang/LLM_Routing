import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y1 - y2)**2)

def verify_solution(tour, total_travel_cost, maximum_distance):
    # City coordinates indexed by city number
    city_coordinates = [
        (90, 3),   # Depot city 0
        (11, 17),  # City 1
        (7, 27),   # City 2
        (95, 81),  # City 3
        (41, 54),  # City 4
        (31, 35),  # City 5
        (23, 95),  # City 6
        (20, 56),  # City 7
        (49, 29),  # City 8
        (13, 17)   # City 9
    ]

    # Check Requirement 1: Visit each city exactly once and return to depot
    expected_cities = set(range(10))
    visited_cities = set(tour)
    
    if visited_cities != expected_cities or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: Travel cost calculation
    calculated_total_cost = 0
    calculated_max_distance = 0
    
    for i in range(len(tour) - 1):
        city_1 = tour[i]
        city_2 = tour[i + 1]
        distance = calculate_euclidean_distance(*city_coordinates[city_1], *city_coordinates[city_2])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    if not (abs(calculated_total_cost - total_travel_cost) < 0.01 and 
            abs(calculated_max_distance - maximum_distance) < 0.01):
        return "FAIL"

    return "CORRECT"

# Provided solution
tour_solution = [0, 5, 9, 1, 2, 7, 6, 4, 3, 8, 0]
total_travel_cost_solution = 399.36740806410444
maximum_distance_solution = 69.42621983083913

# Test the provided solution
result = verify_solution(tour_solution, total_travel_cost_solution, maximum_distance_solution)
print(result)