import math

# Given solution
solution = {
    'Tour': [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 10, 15, 4, 3, 6, 19, 0],
    'Total travel cost': 408.57128868781365,
    'Maximum distance between consecutive cities': 79.2464510246358
}

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0),
    4: (11, 10), 5: (69, 22), 6: (28, 11), 7: (70, 2),
    8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25),
    16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def verify_solution(solution, cities):
    tour = solution['Tour']
    expected_total_cost = solution['Total travel cost']
    expected_max_distance = solution['Maximum distance between consecutive cities']

    # Check if the tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once (excluding the starting-ending depot)
    if sorted(tour[1:-1]) != sorted(list(cities.keys())[1:]):
        return "FAIL"
    
    # Verify total travel cost and maximum distance
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    
    # Check for float precision issues in comparing costs
    if not math.isclose(total_cost, expected_total_cost, rel_tol=1e-6):
        return "FAIL"
    if not math.isclose(max_distance, expected_max_distance, rel_tol=1e-6):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Run the verification
print(verify_solution(solution, cities))