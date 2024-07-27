import math

# City coordinates redefined
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Tours provided
robot_tours = [
    [0, 16, 5, 22],
    [0, 7, 2, 15],
    [0, 14, 17, 18],
    [0, 21, 11, 1],
    [0, 20, 12, 3],
    [0, 6, 10, 19],
    [0, 4, 8],
    [0, 13, 9]
]

def euclidean_distance(a, b):
    """ Compute the Euclidean distance between two cities, identified by their indices. """
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

def verify_solution(robot_tours, cities):
    all_cities = set(cities.keys())
    visited_cities = set()

    # Verify all tours start from city 0 (depot)
    if not all(tour[0] == 0 for tour in robot_tours):
        return "FAIL: Not all tours start from city 0."

    # Collect all cities from all tours
    for tour in robot_tours:
        for city in tour:
            visited_cities.add(city)

    # Check if all required cities are visited exactly once
    if visited_cities != all_cities:
        return "FAIL: Not all cities are visited exactly once."

    # Compute the total travel cost
    calculated_total_cost = sum(sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1)) for tour in robot_tours)
    given_total_cost = 401.0290052463142  # Total cost from the proposed solution to verify

    if not math.isclose(calculated_total_cost, given_total_cost, abs_tol=1e-5):
        return f"FAIL: Total travel costs do not match. Calculated: {calculated_total_cost}, Expected: {given_total_cost}"

    return "CORRECT"

# Run verification
print(verify_solution(robot_tours, cities))