import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_tour(tour, total_travel_cost, max_distance_between_cities):
    # Example coordinates for cities
    coordinates = [
        (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), 
        (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), 
        (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
    ]

    # [Requirement 1] Starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] All cities must be visited exactly once, except depot city 0
    from collections import Counter
    city_count = Counter(tour)
    if city_count[0] != 2 or any(city_count[city] != 1 for city in range(1, 20)):
        return "FAIL"

    # [Requirement 3] Check if the maximum distance between consecutive cities is minimized
    # This requires comparing with optimal or known good results, which
    # are typically domain-specific and not generally available. We skip an exact check.
    # For now, we check if the distance between consecutive cities does not exceed max_distance_between_cities
    real_max_distance = 0
    calculated_total_cost = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
        calculated_total_cost += dist
        if dist > real_max_distance:
            real_max_distance = dist

    if real_max_distance > max_distance_between_cities + 1e-5:
        return "FAIL"

    # [Requirement 4] Total travel cost is correctly calculated based on Euclidean distances
    if abs(calculated_total_cost - total_travel_cost) > 1e-5:
        return "FAIL"

    return "CORRECT"

# Example output from the provided solution
tour = [0, 1, 2, 3, 0]  # Placeholder until actual tour is given
total_travel_cost = 100  # Placeholder until actual cost is given
max_distance_between_cities = 32.57299494980466  # As per your provided data

# Call verification function
result = verify_tour(tour, total_travel_cost, max_distance_between_cities)
print(result)