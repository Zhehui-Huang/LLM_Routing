import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, distances, expected_cost):
    # Check if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly 6 cities are visited including the depot city
    if len(set(tour)) != 6:
        return "FAIL"

    # Calculate and check the travel cost
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += calculate_euclidean_distance(distances[tour[i-1]], distances[tour[i]])
    
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# City coordinates
coords = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Provided solution
solution_tour = [0, 8, 5, 2, 1, 9, 0]
provided_cost = 183.85354044487238

# Verify the solution
result = verify_solution(solution_tour, coords, provided_cost)
print(result)