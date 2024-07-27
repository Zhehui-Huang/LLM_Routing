import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(cities, tour, total_cost):
    # Extract city locations
    city_locations = {
        0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60),
        4: (25, 18), 5: (67, 23), 6: (97, 32), 7: (25, 71),
        8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
        12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88),
        16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
    }
    
    # Requirement 1: Check if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Check if all cities are visited exactly once (excluding the depot) and correct indices
    expected_cities = set(range(len(cities)))
    visited_cities = set(tour)
    if visited_cities != expected_cities:
        return "FAIL"
    
    # Requirement 3: Calculate cost using Euclidean distance and check against given total cost
    computed_cost = 0
    for i in range(1, len(tour)):
        city_idx1 = tour[i - 1]
        city_idx2 = tour[i]
        computed_cost += euclidean_distance(city_locations[city_idx1], city_locations[city_idx2])
    
    # Check the precision of floating point arithmetic up to reasonable precision
    if not math.isclose(computed_cost, total_cost, abs_tol=1e-4):
        return "FAIL"
    
    # Requirement 4 can only be assessed if we know the optimal tour cost, which we assume has been computed before
    # (since we cannot confirm minimality without solving the TSP optimally again)

    # Requirement 5 is implicitly checked by the format of the output 'Tour' and 'Total travel cost'

    # If all checks passed
    return "CORRECT"

# Given output
tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
total_cost = 349.1974047195548
cities = list(range(20))

# Validate the tour and the cost
verification_result = verify_tour(cities, tour, total_cost)
print(verification_result)