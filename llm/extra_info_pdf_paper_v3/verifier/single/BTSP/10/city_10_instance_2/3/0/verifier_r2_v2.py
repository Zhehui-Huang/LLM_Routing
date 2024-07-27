import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour(tour, coordinates):
    # Requirement 1: Start and End at Depot City 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit each city exactly once except the depot city
    if sorted(tour[1:-1]) != sorted(list(set(tour[1:-1]))):
        return "FAIL"
    if set(tour[1:-1]) != set(range(1, 10)):
        return "FAIL"
    
    # Calculate total and maximum distances between consecutive cities
    total_distance = 0
    max_distance = 0
    for i in range(len(tour)-1):
        distance = calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
        total_distance += distance
        if distance > max_distance:
            max_distance = distance

    expected_max_distance = 69.42621983083913  # Expected longest distance between any two cities
    expected_total_distance = 418.32344417340323  # Expected total cost

    # Allowing a tolerated error margin due to floating point arithmetic discrepancies
    tolerance = 0.01
    if abs(max_distance - expected_max_distance) > tolerance or abs(total_distance - expected_total_distance) > tolerance:
        return "FAIL"
    
    return "CORRECT"

# Coordinate setup for the cities indexed from 0 to 9
coordinates = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54),
    5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)
}

# Provided solution tour for testing
tour_provided = [0, 5, 1, 2, 9, 7, 6, 4, 3, 8, 0]

# Execute the test and print the result
result = verify_tour(tour_provided, coordinates)
print(result)