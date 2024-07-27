import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour(tour, coordinates):
    # Requirement 1: Start and End at Depot City 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit each city exactly once
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != 9 or set(range(1, 10)) != unique_cities:
        return "FAIL"
    
    # Requirement 3: Check distances
    max_distance = 69.42621983083913
    actual_max_distance = 0
    total_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
        total_distance += distance
        if distance > actual_max_index_distance:
            actual_max_distance = distance
    
    expected_total_distance = 418.32344417340323
    # Allow small floating point variances
    if actual_max_distance > max_distance + 0.01 or abs(total_distance - expected_total_distance) > 0.01:
        return "FAIL"
    
    return "CORRECT"

# Coordinates of the cities (city index: (x, y))
coordinates = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54),
    5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)
}

# Provided solution to test
tour_provided = [0, 5, 1, 2, 9, 7, 6, 4, 3, 8, 0]

# Running the verification function
result = verify_tour(tour_provided, coordinates)
print(result)