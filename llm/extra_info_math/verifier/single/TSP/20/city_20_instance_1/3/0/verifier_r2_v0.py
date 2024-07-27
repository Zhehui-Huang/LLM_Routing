import math

def compute_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour(tour, coordinates, expected_cost):
    # Initial Requirements
    n = len(coordinates)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Ensures all other cities are visited exactly once
    if sorted(tour) != sorted(list(range(n))):
        return "FAIL"
    
    # Calculate actual travel cost
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += compute_euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    
    # Check if the actual cost is equivalent to the expected cost (could vary due to computational precision)
    if not math.isclose(actual_cash, expected_cost, abs_tol=1e-9):
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

tour = [0, 6, 9, 2, 12, 13, 1, 8, 18, 15, 19, 17, 16, 11, 10, 4, 7, 5, 14, 3, 0]
expected_cost = 377

result = verify_tour(tour, coordinates, expected_cost)
print(result)