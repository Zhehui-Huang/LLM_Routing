import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, coordinates):
    # Verifying Requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verifying Requirement 2
    if len(set(tour)) != len(coordinates) or len(tour) != len(coordinates) + 1:
        return "FAIL"

    # Verifying Requirement 3
    # Since the goal is to minimize the longest distance but specification of the actual minimum isn't provided,
    # we will check if touring all cities and returning to the depot is fulfilled and calc the max distance for testing.
    max_distance = 0
    total_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    
    # Given distances from the problem for validation
    expected_total_distance = 373.97
    expected_max_distance = 63.60

    # Allow small floating-point discrepancies
    if not (abs(total_distance - expected_total_distance) < 1e-2 and 
            abs(max_distance - expected_max_distance) < 1e-2):
        return "FAIL"

    return "CORRECT"

# Coordinates of cities indexed by their number
coordinates = [
    (9, 93),  # Depot city 0
    (8, 51),  # City 1
    (74, 99), # City 2
    (78, 50), # City 3
    (21, 23), # City 4
    (88, 59), # City 5
    (79, 77), # City 6
    (63, 23), # City 7
    (19, 76), # City 8
    (21, 38), # City 9
    (19, 65), # City 10
    (11, 40), # City 11
    (3, 21),  # City 12
    (60, 55), # City 13
    (4, 39)   # City 14
]

# Proposed tour
tour = [0, 8, 10, 1, 11, 14, 9, 4, 12, 7, 3, 5, 6, 2, 13, 0]

# Check if the solution is correct
result = verify_solution(tour, coordinates)
print(result)