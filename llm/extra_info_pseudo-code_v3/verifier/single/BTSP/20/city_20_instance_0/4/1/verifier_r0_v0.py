import math

# City coordinates including the depot city 0
city_positions = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18),
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tour, total_travel_cost, max_consec_distance):
    # Requirement 1
    if len(city_positions) != 20:
        return "FAIL"
    
    # Requirement 2
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 3
    unique_cities = set(tour)
    if len(unique_cities) != 20 or len(tour) != 21:
        return "FAIL"
    
    # Requirement 5
    # Calculating actual distances and total travel cost
    calculated_travel_cost = 0
    calculated_max_consec_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_euclidean_distance(city_positions[tour[i]], city_positions[tour[i + 1]])
        calculated_travel_cost += distance
        if distance > calculated_max_consec_distance:
            calculated_max_consec_distance = distance
            
    # Requirement 7
    if not math.isclose(calculated_travel_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"
    
    # Requirement 8
    if not math.isclose(calculated_max_consec_distance, max_consec_distance, rel_tol=1e-5):
        return "FAIL"
    
    # All checks passed
    return "CORRECT"

# Solution provided
tour = [0, 4, 1, 8, 13, 17, 5, 19, 2, 6, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
total_travel_cost = 351.47400150224905
max_consec_distance = 32.38826948140329

# Run test
result = test_solution(tour, total_travel_cost, max_consec_distance)
print(result)