import math

def calculate_euclidean_distance(pt1, pt2):
    return math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

def verify_tour(tour, cost):
    # Coordinates of each city
    coordinates = [
        (54, 87),  # City 0
        (21, 84),  # City 1
        (69, 84),  # City 2
        (53, 40),  # City 3
        (54, 42),  # City 4
        (36, 30),  # City 5
        (52, 82),  # City 6
        (93, 44),  # City 7
        (21, 78),  # City 8
        (68, 14),  # City 9
        (51, 28),  # City 10
        (44, 79),  # City 11
        (56, 58),  # City 12
        (72, 43),  # City 13
        (6, 99)    # City 14
    ]

    # Requirements Validation
    # Requirement 1 and 4
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2
    if sorted(tour) != sorted(list(range(16))):
        return "FAIL"
    
    # Requirement 3 and 5
    calculated_cost = sum(calculate_euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))
    if not math.isclose(calculated_cost, cost, rel_tol=1e-9):  # Using isclose to avoid floating point precision issues
        return "FAIL"
    
    return "CORRECT"

# Provided tour and cost
given_tour = [0, 14, 13, 4, 3, 12, 2, 10, 5, 9, 7, 6, 11, 8, 1, 0]
given_cost = 479.0

# Validate the given solution
result = verify_tour(given_tour, given_cost)
print(result)