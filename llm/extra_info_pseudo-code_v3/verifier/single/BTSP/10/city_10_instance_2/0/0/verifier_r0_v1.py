import math

def compute_euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def verify_solution(tour, total_travel_cost, max_distance_between_cities):
    # City coordinates
    coordinates = {
        0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81),
        4: (41, 54), 5: (31, 35), 6: (23, 95), 7: (20, 56), 
        8: (49, 29), 9: (13, 17)
    }
    
    # [Requirement 1] Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Each city visited exactly once
    if len(set(tour)) != len(tour):
        return "FAIL"
    
    # [Requirement 5] Tour starts and ends at depot city 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # Calculate actual total travel cost and max distance
    actual_total_cost = 0
    actual_max_distance = 0
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i + 1]
        distance = compute_euclidean_distance(coordinates[city_from], coordinates[city_to])
        actual_total_cost += distance
        actual_max_distance = max(actual_max_distance, distance)
    
    # [Requirement 6] Check computed total travel cost
    if not math.isclose(total_travel_cost, actual_total_cost, rel_tol=1e-6):
        return "FAIL"
    
    # [Requirement 7] Check maximum distance between consecutive cities
    if not math.isclose(max_distance_between_cities, actual_max_distance, rel_tol=1e-6):
        return "FAIL"
    
    return "CORRECT"

# Provided solution
tour = [0, 5, 1, 2, 9, 7, 6, 4, 3, 8, 0]
total_travel_cost = 418.32344417340323
max_distance_between_cities = 69.42621983083913

# Run verification
print(verify_solution(tour, total_travel_data. explorowingice="Edirectpping_resourcehtance_be funder_be", oposing_burger = at DULE DAY_HEREthreshold_phau.)