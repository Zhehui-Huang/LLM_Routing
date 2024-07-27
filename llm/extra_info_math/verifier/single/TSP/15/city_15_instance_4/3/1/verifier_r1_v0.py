import math

# Given solution and tour cost
solution_tour = [0, 1, 5, 9, 2, 7, 4, 12, 11, 6, 3, 8, 14, 13, 10, 0]
reported_cost = 288.5242816725832

# City coordinates as provided
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39),
}

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour(tour, reported_cost):
    n = len(cities)
    
    # Verify Requirement 1: Tour completeness and return
    if tour[0] != 0 or tour[-1] != 0 or len(set(tour)) != n:
        return "FAIL"
    
    # Verify Requirement 2 and 3: Each city visited and left exactly once
    visit_count = {i: 0 for i in range(n)}
    for city in tour:
        visit_count[city] += 1
        if visit_count[city] > 2:  # More than once visited and once left since start and end at depot
            return "FAIL"

    # Subtour elimination is intrinsic in the path if above is correct in a closed tour starting and ending at depot

    # Verify Requirement 5: Calculate and verify the reported total cost
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(actual_cost, reported_cost, abs_tol=1e-6):
        return "FAIL"

    return "CORRECT"

# Perform the test
result = verify_tour(solution_tour, reported_cost)
print(result)