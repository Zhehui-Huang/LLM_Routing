import math

def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def test_solution():
    # City coordinates
    cities = {
        0: (14, 77),
        1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
        5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
        10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
        15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
    }

    # City groups
    groups = [
        [5, 6, 7, 11, 17],
        [1, 4, 8, 13, 16],
        [2, 10, 15, 18, 19],
        [3, 9, 12, 14]
    ]

    # Proposed solution
    tour = [0, 14, 0, 14, 0, 14, 0, 14, 0, 14, 0, 14, 0, 14, 0, 14, 0, 14, 0, 14, 0, 0]
    reported_cost = 145.6021977856104

    # Test [Requirement 1]
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"

    # Test [Requirement 2]
    visited = []
    for segment in range(len(tour) - 1):
        city = tour[segment]
        for group in groups:
            if city in group:
                visited.append(city)
                break

    if not all(len(set(group) & set(visited)) == 1 for group in groups):
        return "FAIL"

    # Test [Requirement 3]
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    if not abs(calculated_cost - reported_cost) < 0.0001:  # allow for small numerical discrepancies
        return "FAIL"

    return "CORRECT"

# Printing the result of the test
print(test_solution())