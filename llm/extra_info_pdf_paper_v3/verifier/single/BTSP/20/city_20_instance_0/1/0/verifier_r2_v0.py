import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, total_travel_cost, max_distance_between_cities, cities):
    # Requirement 1: Tour starts and ends at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city visited exactly once
    if sorted(tour) != sorted(list(set(tour)) + [0]):
        return "FAIL"
    
    # Computing the actual total travel cost and the maximum distance
    computed_total_cost = 0
    computed_max_distance = 0
    for i in range(len(tour)-1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        computed_total_cost += distance
        if distance > computed_max_distance:
            computed_max_distance = distance
    
    # Check computed vs provided distance metrics
    if not math.isclose(total_travel_cost, computed_total_cost, abs_tol=1e-2):
        return "FAIL"
    
    if not math.isclose(max_distance_between_cities, computed_max_distance, abs_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Cities coordinates (index corresponds to city number)
cities = [
    (8, 11),   # Depot city
    (40, 6),   # City 1
    (95, 33),  # City 2
    (80, 60),  # City 3
    (25, 18),  # City 4
    (67, 23),  # City 5
    (97, 32),  # City 6
    (25, 71),  # City 7
    (61, 16),  # City 8
    (27, 91),  # City 9
]

# Provided solution details
tour = [0, 1, 2, 3, 9, 7, 4, 5, 6, 8, 0]
total_travel_cost = 425.29
max_distance_between_cities = 61.4

# Run the test
result = verify_tour(tour, total_travel_cost, max_distance_between_cities, cities)
print(result)