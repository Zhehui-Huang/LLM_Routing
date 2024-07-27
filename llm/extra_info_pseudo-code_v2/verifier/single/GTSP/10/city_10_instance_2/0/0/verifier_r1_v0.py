import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, expected_cost):
    # City coordinates given in the task description
    coordinates = {
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
    
    # City groups validation
    groups = [
        [3, 6],
        [5, 8],
        [4, 9],
        [1, 7],
        [2]
    ]

    # Check each group is represented exactly once
    selected_cities = tour[1:-1]  # exclude the depot city at start and finish
    for group in groups:
        if not any(city in group for city in selected_cities):
            return "FAIL: Not every group is represented."

    # Check for duplicate selections from the same group
    visited = set()
    for city in selected_cities:
        for group in groups:
            if city in group:
                if city in visited:
                    return "FAIL: Duplicate city from a group."
                visited.update(group)  # Add all cities from this group to visited set

    # Tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at the depot city 0."

    # Calculate the total cost of the tour
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])

    # Check if calculated total cost matches the given expected cost
    if abs(total_cost - expected_cost) > 1e-2:  # allow some floating-point error tolerance
        return f"FAIL: Expected cost mismatch. Calculated: {total_cost}, Expected: {expected_cost}"

    return "CORRECT"

# Given tour and cost from the task solution attempt
tour_test = [0, 3, 5, 9, 1, 2, 0]
expected_cost_test = 281.60

# Output the test result
print(verify_solution(tour_test, expected_cost_test))