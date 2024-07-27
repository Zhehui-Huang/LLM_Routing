import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def test_solution(tour, total_travel_cost, max_distance):
    cities = [
        (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
        (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
        (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
        (50, 28), (69, 9)
    ]

    # [Requirement 1] Checks if all cities are visited exactly once
    if len(tour) != len(cities) + 1:
        return "FAIL"
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if len(set(tour)) != len(cities) + 1:
        return "FAIL"

    # Calculating total travel cost and checking max distance
    calculated_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_cost += dist
        calculated_max_distance = max(calculated_max_distance, dist)

    # [Requirement 4] Checks the total travel cost
    if not math.isclose(calculated_cost, total_travel_customer, rel_tol=1e-2):
        return "FAIL"

    # [Requirement 5] Checks the maximum distance between any two consecutive cities
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Provided solution details
tour = [0, 3, 5, 7, 4, 10, 11, 16, 17, 15, 19, 18, 1, 2, 8, 12, 13, 9, 6, 14, 0]
total_travel_cost = 440.74
max_distance = 32.57

# Validate the provided solution
result = test_solution(tour, total_travel_cost, max_distance)
print(result)