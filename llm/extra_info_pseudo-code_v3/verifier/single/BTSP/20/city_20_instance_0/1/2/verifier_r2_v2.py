import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def test_solution(tour, cities, expected_total_cost, expected_max_distance):
    # Check if tour starts and ends at the depot city (Requirement 1)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each city is visited exactly once (Requirement 1)
    if set(tour) != set(range(len(cities))):
        return "FAIL"
    
    # Calculate and check the travel costs (Requirements 2 & 3)
    total_cost = 0
    max_distance = 0
    
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i + 1]
        distance = calculate_distance(cities[city_from], cities[city_to])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance

    # Determine if the calculated travel cost matches the provided cost (Requirement 3)
    if not math.isclose(total_cost, expected_total_cost, abs_tol=1e-2):
        return "FAIL"
    
    # Determine if the calculated max distance matches the provided max distance (Requirement 2)
    if not math.isclose(max_distance, expected_max_distance, abs_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Given cities coordinates
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71), 
    (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), 
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Given solution output
tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
total_travel_cost = 349.1974047195548
max_distance_between_consecutive_cities = 32.38826948140329

# Validate the solution using a test
result = test_solution(tour, cities, total_travel_leg, cost, and max_cities_distance_between_consecutive) #=> CORRECT
print(result)