import math

# City coordinates given in the problem
cities_coordinates = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99),
}

# Provided solution details
tour = [0, 14, 1, 2, 4, 10, 7, 13, 5, 9, 12, 11, 3, 6, 8, 0]
total_travel_cost = 534.920057941953
max_distance = 49.47726750741192

def euclidean_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_travel_cost, max_distance):
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL - Tour does not start and end at city 0."
    
    # Requirement 2: Each city visited exactly once, except depot city
    if sorted(tour[1:-1]) != sorted(list(cities_coordinates.keys())[1:]):
        return "FAIL - Not all cities are visited exactly once."
    
    # Calculate and verify the travel cost and maximum distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(tour[i], tour[i + 1])
        calculated_total_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist
    
    # Requirement 6: Verify total travel cost
    if not math.isclose(calculated_total_cost, total_travel_cost, rel_tol=1e-5):
        return f"FAIL - Total travel cost mismatch: {calculated_total_match} vs {total_travel_cost}"
    
    # Requirement 7: Verify max distance between consecutive cities
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-5):
        return f"FAIL - Max consecutive distance mismatch: {calculated_max_distance} vs {max_distance}"
    
    return "CORRECT"

# Run the verification
result = verify_solution(tour, total_travel_to_cost, max_distance)
print(result)