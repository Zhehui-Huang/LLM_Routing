import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_tour():
    cities = {
        0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22), 6: (28, 11),
        7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73),
        14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
    }
    proposed_tour = [10, 15, 4, 3, 6, 12, 7, 16, 5, 9, 2, 14, 11, 1, 13, 18, 17, 8, 19, 0]
    proposed_cost = 345.59266139889314

    # Requirement 1
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"

    # Requirement 2
    visited = set(proposed_tour)
    if len(visited) != 20 or 0 not in visited:
        return "FAIL"

    # Requirement 4 & 5
    if len(proposed_tour) != 20:
        return "FAIL"

    # Calculate cost and check Requirement 3
    total_calculated_cost = 0
    for i in range(len(proposed_tour) - 1):
        city1 = proposed_tour[i]
        city2 = proposed_tour[i + 1]
        total_calculated_cost += euclidean_distance(*cities[city1], *cities[city2])

    if not math.isclose(proposed_cost, total_calculated_cost, abs_tol=1e-5):
        return "FAIL"

    # All checks passed
    return "CORRECT"

# Run the verification test
verification_result = verify_tour()
print(verification_result)