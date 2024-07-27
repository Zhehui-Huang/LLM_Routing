import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def verify_solution(tour, reported_cost):
    cities_positions = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]
    
    # Requirement 1: Check exactly 8 cities are visited including the depot
    if len(set(tour)) != 9 or tour.count(0) != 2:  # including depot twice and 7 other distinct cities
        return "FAIL"
    
    # Requirement 2: Check that the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 3: Validate the total travel cost using the Euclidean distance
    calculated_cost = 0
    for i in range(1, len(tour)):
        city1 = tour[i - 1]
        city2 = tour[i]
        x1, y1 = cities_positions[city1]
        x2, y2 = cities_positions[city2]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Provided tour and cost
tour = [0, 3, 6, 9, 1, 5, 7, 4, 0]
total_travel_cost = 235.37735391753955

# Verification
result = verify_solution(tour, total_travel_cost)
print(result)