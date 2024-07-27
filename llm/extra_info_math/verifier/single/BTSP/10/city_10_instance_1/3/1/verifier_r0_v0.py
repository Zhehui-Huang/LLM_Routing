import math

# Data for the cities coordinates
cities_coords = {
    0: (53, 68), 
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two cities"""
    return math.sqrt((cities_coords[city1][0] - cities_coords[city2][0]) ** 2 + (cities_coords[city1][1] - cities_coords[city2][1]) ** 2)

def verify_solution(tour, total_cost, max_distance):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Tour must start and end at depot city 0.
    
    if len(set(tour)) != len(cities_coords):
        return "FAIL"  # All cities must be visited exactly once + return to the depot.
    
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        distance = calculate_distance(city_a, city_b)
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    # Check if the Euclidean calculation is applied and if the round of calculated values might differ 
    # due to floating-point precision when comparing to given total_cost and max_distance.
    if not math.isclose(calculated_total (total_cost, abs_tol=1e-2) or not math.isclose(calculated_max_distance, max_distance, abs_tol=1e-2):
        return "FAIL"  # Extraction and calculation mismatch testing within reasonable tolerance.
    
    return "CORRECT"

# Given result
tour = [0, 8, 3, 4, 5, 2, 9, 7, 1, 6, 0]
total_travel_cost = 302.74
maximum_distance = 56.61

# Verify
result = verify_solution(tour, total_travel_cost, maximum_distance)
print(result)