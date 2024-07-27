import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def check_requirements(tour, reported_cost):
    # Define the city coordinates
    cities = {
        0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
        5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
        10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
    }

    # [Requirement 1]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2]
    if sorted(tour[1:-1]) != list(range(1, 15)):
        return "FAIL"

    # [Requirement 3 & 5]
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    if abs(computed_cost - reported_cost) > 1e-6:
        return "FAIL"

    return "CORRECT"

# Given solution
tour = [0, 1, 10, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 8, 0]
reported_cost = 1069.7596061377574

# Verify and assert the result
result = check_requirements(tour, reported_cost)
print(result)