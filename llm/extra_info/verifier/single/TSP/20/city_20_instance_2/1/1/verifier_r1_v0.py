import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tour, total_cost, locations):
    # Verify requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify requirement 2
    if len(tour) != len(set(tour)):
        return "FAIL"
    
    if set(tour) != set(range(len(locations))):
        return "FAIL"

    # Check the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(locations[tour[i]], locations[tour[i + 1]])

    # Verify requirement 3 and 5
    if not math.isclose(total_cost, calculated_cost, rel_tol=1e-5):
        return "FAIL"

    # Verify requirement 4 is inherently checked by the tour format check

    return "CORRECT"

# Provided cities coordinates
locations = [
    (3, 26),   # Depot city 0
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48),  # City 19
]

# Provided tour and total cost
tour = [0, 12, 14, 16, 19, 11, 7, 18, 13, 15, 5, 1, 17, 4, 3, 10, 8, 6, 9, 2, 0]
total_cost = 478.4306776278287

# Validation
result = verify_solution(tour, total_cost, locations)
print(result)