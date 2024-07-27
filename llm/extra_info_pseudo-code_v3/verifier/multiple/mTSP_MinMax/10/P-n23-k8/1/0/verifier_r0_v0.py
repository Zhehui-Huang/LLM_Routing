import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution():
    # Coordinates for cities including the depot
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),  5: (52, 33),
        6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
        12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
        18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
    }

    # Solution provided
    tours = [
        [0, 2, 8, 9, 13, 0],
        [0, 3, 12, 15, 0],
        [0, 6, 21, 0],
        [0, 14, 17, 0],
        [0, 1, 10, 16, 0],
        [0, 18, 19, 0],
        [0, 4, 11, 0],
        [0, 5, 7, 20, 22, 0]
    ]

    # Verify Requirement 3 - All cities (except depot) visited exactly once
    visited = {i:0 for i in range(1, 23)}
    for tour in tours:
        for city in tour[1:-1]:  # Exclude depot city at start and end
            visited[city] += 1

    if any(v != 1 for v in visited.values()):
        print("FAIL: Not all cities are visited exactly once or are visited multiple times.")
        return "FAIL"

    # Calculate and verify costs
    expected_costs = [86.16, 78.2, 24.48, 69.36, 42.67, 89.42, 57.39, 77.66]
    max_travel_cost = 89.42
    calculated_costs = []

    for tour, expected_cost in zip(tours, expected_costs):
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_costs.append(total_cost)
        if not math.isclose(total_cost, expected_cost, rel_tol=1e-2):
            print(f"FAIL: Expected cost does not match calculated cost for a tour. Expected: {expected_cost}, Calculated: {total_cost}")
            return "FAIL"

    # Verify Requirement 5 - Minimize the maximum distance
    if not math.isclose(max(calculated_costs), max_travel_cost, rel_tol=1e-2):
        print(f"FAIL: The maximum travel cost calculated ({max(calculated_costs)}) does not match the expected ({max_travel_cost}).")
        return "FAIL"

    return "CORRECT"

# Print the test result
print(verify_solution())