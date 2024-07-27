import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_cost, max_distance):
    # Given coordinates
    coordinates = [
        (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
        (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), 
        (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), 
        (60, 63), (93, 15)
    ]

    # Check requirement 1: Start and end at depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check requirement 2: Visit each city exactly once except for the depot which needs to be visited twice
    if sorted(tour) != [i for i in range(20)] + [0]:
        return "FAIL"

    # Check requirement 3 & 5 & 6 & 7: Properly calculate distances
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        distance = euclidean_distance(*coordinates[city1], *coordinates[city2])
        calculated_total_cost += distance
        calculated_max_distance = max(calculated_max_distance, distance)

    # Requirement 6: Check total travel cost
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-9):
        return "FAIL"

    # Requirement 7: Check maximum distance between consecutive cities
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Given solution details
tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
total_cost = 349.2
max_distance = 32.39

# Run the verification
result = verify_solution(tour, total_cost, max_distance)
print(result)  # Output "CORRECT" if all checks pass, otherwise "FAIL"